# ansible-flask-gunicorn-nginx
This is a project to learn how to work with anisble. I will take it in increments, first with a single server for a flask app then extending that to seperate db, redis and rabbitmq servers and then later clustering it all for HA.

## Gunicorn
We create a simple systemd service file that runs 3 gunicorn workers for our app, we then move it to it's location and reload the daemon.

## Nginx
Simple install of Nginx and a simple config that points to our flask application and serves it on port 80. #TODO: change ip

## Flask
A simple flask app structure with a possibility to grow but I would not recommend deploying this with ansible, just added it for testing purposes. 
