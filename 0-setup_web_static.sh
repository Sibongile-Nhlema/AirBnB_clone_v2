#!/usr/bin/env bash
# Set up web servers for deployment of web static
# Install Nginx
if ! command -v nginx &> /dev/null; then
  sudo apt-get update
  sudo apt-get -y install nginx
fi

# Create directories
if [ ! -d "/data/" ]; then
  mkdir /data/
fi
if [ ! -d "/data/web_static/" ]; then
  mkdir -p /data/web_static/
fi
if [ ! -d "/data/web_static/releases/" ]; then
  mkdir -p /data/web_static/releases/
fi
if [ ! -d "/data/web_static/shared/" ]; then
  mkdir -p /data/web_static/shared/
fi
if [ ! -d "/data/web_static/releases/test/" ]; then
  mkdir -p /data/web_static/releases/test/
fi

# Create html file
echo "<html><head><title>Test</title></head><body><h1>Hello</h1></body></html>" > /data/web_static/releases/test/index.html

# Create a symbolic link
if [ -L "/data/web_static/current" ]; then
  rm /data/web_static/current
fi
sudo ln -s /data/web_static/releases/test/ /data/web_static/current

# Change ownership of /data/
chown -R ubuntu:ubuntu /data/

# Serve the content of /data/web_static/current/ to hbnb_static
hbnb_static_content="server_name _;\n\n\tlocation \/hbnb_static {\n\t\talias \/data\/web_static\/current\/;\n\t}"
sudo sed -i "s/server_name _;/$hbnb_static_content/" /etc/nginx/sites-available/default

sudo service nginx restart
