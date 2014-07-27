#
# Python3/bottle web server Dockerfile
#
# This image demonstrates how to set up a Python3/bottle web application using
# the base image pablosan/bottle-py3 as a starting point.
#
# https://github.com/Pablosan/hello-bottlepy
#

# Pull base image
FROM pablosan/bottle-py3

# Install the app
ADD hello-bottlepy /opt/hello-bottlepy

# Expose ports
EXPOSE 8003

# Define default command
ENTRYPOINT ["/usr/bin/python3", "/opt/hello-bottlepy/server.py"]
