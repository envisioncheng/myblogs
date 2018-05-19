[Unit]
Description=uWSGI instance to serve myblogs
After=network.target

[Service]
User=ubuntu
Group=www-data
WorkingDirectory=/home/ubuntu/myblogs
Environment="PATH=/home/ubuntu/.virtualenvs/myenv/bin"
ExecStart=/home/ubuntu/.virtualenvs/myenv/bin/uwsgi --ini /home/ubuntu/myblogs/myblogs.ini

[Install]
WantedBy=multi-user.target
