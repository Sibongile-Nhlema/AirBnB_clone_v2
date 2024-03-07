#!/usr/bin/env bash
# Script that sets up web server for the deployment of web_static

# Install Nginx
sudo apt-get update
sudo apt-get install nginx -y

# Create /data
sudo mkdir -p /data

# Create /data/web_static/
sudo mkdir -p /data/web/static/

# Create /data/web_static/releases/
sudo mkdir -p /data/web_static/releases

# Create /data/web_static/shared/
sudo mkdir -p /data/web_static/shared/

# Create /data/web_static/releases/test/
sudo mkdir -p /data/web_static/releases/test/

# Create a fake HTML file /data/web_static/releases/test/index.html
sudo echo "<html>
	<head>
	<title>Task 0</title>
	</head>
	<body>
	<p>Welcome to TownsVille</p>
	</body>
	</html> " > sudo tee /data/web_static/releases/test/index.html

# Create Symbolic link between /data/web_static/current
# and /data/web_static/releases/test/
# Delete this file and recreate it everytime the script is run

path_link="/data/web_static/current"
target="/data/web_static/releases/test/"

if [ -L "$path_link" ]; then
	sudo rm "$path_link"
fi

sudo ln -s "$target" "$path_link"

sudo echo "Symbolic link created"

# Give ownership of /data/ to ubuntu user and group
sudo chown -R ubuntu:ubuntu /data

# Update the Nginx Configuration to serve the content of /data/web_static/current/ to hbnb_static

nginx_config="/etc/nginx/sites-available/default"
web_static_path="/data/web_static/current/"
alias_path="/hbnb_static"

if ! grep -q "$alias_path" "$nginx_config"; then
    sudo sed -i "/location \/ {/a location $alias_path {\\n  alias $web_static_path;\\n}" "$nginx_config"
fi

sudo service nginx restart
