from fabric.api import *
from fabric.utils import abort
from fabric.contrib.files import append, upload_template
from ConfigParser import SafeConfigParser
import os.path

env.hosts = ['molluscref-uat.qc.to']


@task
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

@task
def bootstrap_ubuntu():
    """
    Bootstrap Ubuntu

    Perform all the initial setup, only run once
    """
    server = UbuntuServer()
    with settings(user='ubuntu'):
        server.install_requirements()
        server.install_webserver()
        server.install_database()
        server.create_appuser()
        server.create_database()
        server.setup_upstart()
        server.setup_nginx_site()
        push_key()
    server.create_deploydir()
    server.create_virtualenv()
    

'apt-get install supervisor'


def deploy():
    pull_code()
    install_requirements()


def postgres(command):
    return sudo(command, user='postgres')


def psql(command):
    return sudo('echo "%s" | psql' % command, user='postgres')


class UbuntuServer():
    def install_requirements(self):
        sudo('apt-get install git-core python-virtualenv')

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
        with settings(warn_only=True):
            result = run('id -u %s' % env.appuser)
        if result.failed:
            sudo('useradd --create-home %s' % env.appuser)

    def create_database(self):
        """
        Run as the app user
        """
        with settings(warn_only=True):
            result = postgres('createuser --no-createdb --no-createrole --no-superuser %(dbuser)s' % env)
        if result.failed and not "already exists" in result:
            abort("Unable to create DB User")

        psql("alter user %(dbuser)s with password '%(dbpass)s';" % env)

        with settings(warn_only=True):
            result = postgres('createdb --owner %(dbuser)s %(dbname)s' % env)
        if result.failed and not "already exists" in result:
            abort("Unable to create DB")

    def create_deploydir(self):
        with settings(warn_only=True):
#            with cd(env.userhome):
            result = run('git clone %(gitrepo)s %(appname)s' % env)
        if result.failed and not "already exists" in result:
            abort("Unable to clone project code")

    def create_virtualenv(self):
        run('virtualenv environment')

    def setup_cron_tasks(self):
        run('crontab > /tmp/crondump')
        append('/tmp/crondump', )

    def setup_upstart(self):
        context = {
            "description": env.description,
            "project_dir": env.appdir,
            "exec_command": "%(envdir)s/bin/python manage.py run_gunicorn --user=%(appuser)s --bind=%(appbind)s archaeobotany.wsgi:application" % env
        }
        upload_template('deploy/upstart.template', '/etc/init/%s.conf' % env.appuser, context, use_sudo=True)

    def setup_nginx_site(self):
        upload_template('deploy/nginx.template', '/etc/nginx/sites-available/%s' % env.appuser, env, use_sudo=True)
        sudo('ln -sf /etc/nginx/sites-available/%(appuser)s /etc/nginx/sites-enabled/%(appuser)s' % env)
        sudo('nginx -t')
        sudo('nginx -s reload')


def read_key_file(key_file):
    key_file = os.path.expanduser(key_file)
    if not key_file.endswith('pub'):
        raise RuntimeWarning('Trying to push non-public part of key pair')
    with open(key_file) as f:
        return f.read()


@task
def push_key(key_file='~/.ssh/id_rsa.pub'):
    key_text = read_key_file(key_file)

    with settings(user=env.sudouser):
        run('id')
        sudo("mkdir -p %(userhome)s/.ssh" % env, user=env.appuser)
        append('%(userhome)s/.ssh/authorized_keys' % env, key_text, use_sudo=True)


@task
def start():
    """
    Start the application
    """
    with settings(user=env.sudouser):
        sudo('initctl start %s' % env.appuser)

@task
def reload():
    """
    Reload the app
    """
    with settings(user=env.sudouser):
        sudo('reload %s' % env.appuser)


@task
def update():
    run('pwd')
    run('id')
    with cd(env.appdir):
        run('git pull')
        with prefix('source ' + env.envdir + '/bin/activate'):
            run('pip install --requirement=%s' % 'requirements.txt')
            run('./manage.py collectstatic --noinput')
            run('./manage.py reset --noinput botanycollection')
            run('./manage.py syncdb')
#            run('./manage.py rebuild_index --noinput')

@task
def update_local_libs():
    with cd(env.appdir):
        with prefix('source ' + env.envdir + '/bin/activate'):
            run('pip install --upgrade git+git://github.com/omad/django-bulkimport.git#egg=django-bulkimport')


@task
def destroy_changes():
    """
    Delete an destroy any remote code changes
    """
    with cd(env.appdir):
        run('git checkout .')


@task
def restart():
    run('supervisorctl -c %(supervisord_cfg)s restart django' % env)


@task
def blast_database():
    env.user = 'ubuntu'
    postgres('dropdb %(dbname)s' % env)
    postgres('createdb --owner %(dbuser)s %(dbname)s' % env)


config()
