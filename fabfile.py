from fabric.api import *
from fabric.contrib.files import append
from ConfigParser import SafeConfigParser
from django.template import Template, Context
import os.path

env.hosts = ['molluscref-uat.qc.to']


def test():
    print env.user + '@' + env.hostname


def config(section='uat'):
    """
    Load settings from deployment.ini

    Load the selected sections options into the env
    """
    parser = SafeConfigParser()
    parser.read('deployment.ini')
    options = parser.options(section)
    for option in options:
        env[option] = parser.get(section, option)


def bootstrap_ubuntu():
    """
    Bootstrap Ubuntu

    Perform all the initial setup, only run once
    """
    env.user = 'ubuntu'
    server = UbuntuServer()
    server.install_requirements()
    server.install_webserver()
    server.install_database()
    server.create_appuser()
    server.create_database()
    server.create_deploydir()
    server.create_virtualenv()
    server.install_appserver()

'apt-get install supervisor'


def deploy():
    pull_code()
    install_requirements()


def postgres(command):
    sudo(command, user='postgres')


def psql(command):
    sudo('echo "%s" | psql' % command, user='postgres')


class UbuntuServer():
    def install_requirements(self):
        sudo('apt-get install git-core')

    def install_pil_reqs(self):
        sudo('apt-get install libjpeg62-dev  zlib1g-dev')

        # For 64bit ubuntu
        sudo('ln -s /usr/lib/x86_64-linux-gnu/libz.so /usr/lib/')
        sudo('ln -s /usr/lib/x86_64-linux-gnu/libjpeg.so /usr/lib')

    def install_webserver(self):
        sudo('apt-get install nginx')

    def install_database(self):
        sudo('apt-get install postgresql libpq-dev python-dev')

    def create_appuser(self):
        sudo('adduser %s %s', self.appname)

    def create_database(self):
        postgres('createuser %(dbuser)s' % env)
        psql("alter user %(dbuser)s with password '%(dbpass)s;" % env)
        postgres('createdb --owner %(dbuser)s %(dbname)s' % env)

    def create_deploydir(self):
        sudo('')
        pass

    def create_virtualenv(self):
        sudo('apt-get install python-virtualenv')
        run('virtualenv environment')


def read_key_file(key_file):
    key_file = os.path.expanduser(key_file)
    if not key_file.endswith('pub'):
        raise RuntimeWarning('Trying to push non-public part of key pair')
    with open(key_file) as f:
        return f.read()


@task
def push_key(key_file='~/.ssh/id_rsa.pub'):
    key_text = read_key_file(key_file)
    append('~/.ssh/authorized_keys', key_text)


def place_config_file(template, final_location):
    # Prepare context
    c = Context()
    for item, value in env.items():
        c[item] = value

    with open(template) as f:
        t = Template(f.read())

    append(final_location, t.render(c), use_sudo=True)


@task
def update():
    run('pwd')
    run('id')
    with cd(env.appdir):
        run('git pull')
        with prefix('source ' + env.envdir + '/bin/activate'):
            run('pip install --requirement=%s' % 'requirements.txt')
            run('./manage.py collectstatic --noinput')
            run('./manage.py syncdb')
            run('./manage.py rebuild_index --noinput')
    run('supervisorctl -c %(supervisord_cfg)s restart django' % env)


@task
def blast_database():
    env.user = 'ubuntu'
    postgres('dropdb %(dbname)s' % env)
    postgres('createdb --owner %(dbuser)s %(dbname)s' % env)


config()
