to SSH in:
ssh inlyst
or
ssh root@172.104.194.142
or
ssh -o PubkeyAuthentication=no root@172.104.194.142

to create a remote repository:
create it in git, such as new_repo
git init
git remote add origin git@personal:jande48/new_repo.git

Make sure to export the packages you need with pip3 freeze > requirements.txt
Make sure you start the cron job with python manage.py crontab add

Here's a summary of how to deploy:

You need to have two users: root and someone else.  
The root user can create and edit the nginx conf file, but
it has to be another user that runs the uwsgi

pip install uwsgi
pip install python3.Y-dev where Y is the version

Make sure you go into your project names directory and change the wsgi.py file to have:

import sys
sys.path.append("/opt/inlyst/project/inlyst_backend")
sys.path.append("/opt/inlyst/venv/Lib/site-packages")

As a root user on the server:
sudo apt-get install nginx
sudo /etc/init.d/nginx start

cd /etc/nginx/sites-available
nano inlyst.conf

# inlyst.conf

# the upstream component nginx needs to connect to

upstream django {

    server unix:///opt/inlyst/project/inlyst_backend/inlyst_backend.sock; # for a file socket
    # server 0.0.0.0:8001;

}

# configuration of the server

server { # the port your site will be served on
listen 80; # the domain name it will serve for
server_name 172.104.194.142;
charset utf-8;

    # max upload size
    client_max_body_size 75M;

    # Django media
    #location /media  {
    #    alias /opt/inlyst/project/inlyst_backend/static;
    #}

    location /static {
        alias /opt/inlyst/project/inlyst_backend/inlyst_backend/static;
    }

    # Finally, send all non-media requests to the Django server.
    location / {
        include /opt/inlyst/project/inlyst_backend/uwsgi_params;
        uwsgi_pass  unix:///opt/inlyst/project/inlyst_backend/inlyst_backend.sock;
    }

}

then still as the root user:
sudo ln -s /etc/nginx/sites-available/inlyst.conf /etc/nginx/sites-enabled/
systemctl daemon-reload
systemctl restart nginx

then switch to your other user

cd /your/project

test that uwsgi works with

uwsgi --ini uwsgi.ini

if it works, then make the uwsgi service
switch back to root user

cd /etc/systemd/system/
nano uwsgi.service

[Unit]
Description=uWSGI instance to serve inlyst
After=network.target

[Service]
User=deploy
Group=www-data
WorkingDirectory=/opt/inlyst/project/inlyst_backend/
Environment="PATH=/opt/inlyst/venv/bin"
ExecStart=/opt/inlyst/venv/bin/uwsgi --ini uwsgi.ini

[Install]
WantedBy=multi-user.target

To Reset A Postgres DB:
sudo su postgres
psql
drop database your_database_name;
create database your_database_name with owner user_you_use_in_django;
\q
