#!/usr/bin/python3
# Script that sets up web server for the deployment of web_static

# Install Nginx
sudo apt update
sudo apt install nginx -y

# Create /data
mkdir /data

# Create /data/web_static/
mkdir /data/web/static/

# Create /data/web_static/releases/
mkdir /data/web_static/releases

# Create /data/web_static/shared/
mkdir /data/web_static/shared/

# Create /data/web_static/releases/test/
mkdir /data/web_static/releases/test/

# Create a fake HTML file /data/web_static/releases/test/index.html
echo "Welcome to TownsVille" > /data/web_static/releases/test/index.html

# Create Symbolic link between /data/web_static/current
# and /data/web_static/releases/test/
# Delete this file and recreate it everytime the script is run

path_link="/data/web_static/current"
target="/data/web_static/releases/test/"

if [ -L "$path_link" ]; then
	rm "$path_link"
fi

ln -s "$target" "$path_link"

echo "Symbolic link created"

# Give ownership of /data/ to ubuntu user and group
sudo chown -R ubuntu:ubuntu /data

# Update the Nginx Configuration to serve the content of /data/web_static/current/ to hbnb_static

nginx_config="/etc/nginx/sites-available/default"
web_static_path="/data/web_static/current/"
alias_path="/hbnb_static"

echo "location $alias_path {" | sudo tee -a "$nginx_config"
echo "	alias $web_static_path;" | sudo tee -a "$nginx_config"
echo "}" | sudo tee -a "$nginx_config"

sudo service nginx restart
