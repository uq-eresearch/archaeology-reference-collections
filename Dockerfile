FROM debian:9

RUN DEBIAN_FRONTEND=noninteractive && \
  apt-get update && \
  apt-get install -y \
    curl \
    git \
    libboost-python-dev \
    libgraphicsmagick++1-dev \
    libjpeg62-turbo-dev \
    libldap2-dev \
    libpq-dev \
    libsasl2-dev \
    nginx \
    postgresql \
    postgresql-contrib \
    python-dev \
    python-pip

# Install S6 to do process management
RUN curl -L https://github.com/just-containers/s6-overlay/releases/download/v1.21.0.2/s6-overlay-amd64.tar.gz | tar xzv -C /
ENTRYPOINT ["/init"]

ADD . /opt/refcollections/archaeology-reference-collections

ADD etc/nginx/refcollections /etc/nginx/sites-enabled/default

ADD etc/services.d/ /etc/services.d/

RUN mkdir -p /var/log/django

WORKDIR /opt/refcollections/archaeology-reference-collections

RUN pip install -r /opt/refcollections/archaeology-reference-collections/requirements.txt

RUN DEBIAN_FRONTEND=noninteractive && \
  echo "en_AU.UTF-8 UTF-8" > /etc/locale.gen && \
  locale-gen en_AU.UTF-8 && \
  /usr/sbin/update-locale LANG=en_AU.UTF-8

ENV LC_ALL=en_AU.UTF-8


