
FROM ubuntu:18.04

# Install required packages and remove the apt packages cache when done.

RUN apt-get update && \
    apt-get upgrade -y && \ 	
    apt-get install -y \
	git \
	python3 \
	python3-dev \
	python3-setuptools \
	python3-pip \
	nginx \
	uwsgi-plugin-python3
	uwsgi-emperor \
	sqlite3 && \
	pip3 install -U pip setuptools && \
   	rm -rf /var/lib/apt/lists/*

# install uwsgi now because it takes a little while

RUN pip3 install uwsgi   	

# setup all the configfiles
RUN echo "daemon off;" >> /etc/nginx/nginx.conf
COPY nginx-app.conf /etc/nginx/sites-available/default
COPY emperoruwsgi.service /etc/supervisor/conf.d/

# COPY requirements.txt and install all dependency packages
COPY webapp/requirements.txt /home/docker/webapp/
RUN pip3 install -r /home/docker/src/webapp/requirements.txt

# Add source code
COPY webapp /home/docker/src/

EXPOSE 80
