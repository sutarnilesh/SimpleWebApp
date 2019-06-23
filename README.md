# SimpleWebApp
This application produces simple webpage for login and logout. Once user login, user see welcome message. This app is served using nginx with docker container.

In order to containerize this application, user must copy all files from docker directory to outside of docker directory.

To build application image
docker build -t simplewebapp .

To run and debug containerized application
docker run -it -p 8001:8001 simplewebapp /bin/bash
