hello-bottlepy
==============

Deploying Python3/bottle web applications just got super simple! Thanks to [Docker](https://www.docker.com/), we can encapsulate our infrastructure nicely and spin up resources quickly, maximizing the time we spend on actually building the app.

This project is an example of how to build upon my [Python3/bottle base image](https://registry.hub.docker.com/u/pablosan/bottle-py3/). This base image is intended to have the essentials for building a bottle app in Python3.

With the base image above as a starting point, creating our app's Docker file and getting our web server up and running couldn't be simpler:

  * Create a Dockerfile that starts with the pablosan/bottle-py3 image and add your application code and specific dependencies.
  * Include your bottle app code in the same repo with the Dockerfile
  * Build your image, and...
  * Deploy!
