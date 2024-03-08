#!/usr/bin/env bash
# Script that sets up web server for the deployment of web_static

# Install Nginx if not already installed
if ! command -v nginx &> /dev/null; then
    sudo apt-get update
    sudo apt-get install nginx -y
fi

# Create necessary directories
sudo mkdir -p /data/web_static/releases/test
sudo mkdir -p /data/web_static/shared

# Create a fake HTML file
echo "<html>
	<head>
		<title>Task 0</title>
	</head>
	<body>
		<p>Welcome to TownsVille</p>
	</body>
</html>" | tee /data/web_static/releases/test/index.html > /dev/null

# Create symbolic link and update ownership
path_link="/data/web_static/current"
target="/data/web_static/releases/test/"
sudo ln -sf "$target" "$path_link"
sudo chown -R ubuntu:ubuntu /data

# Update Nginx configuration
nginx_config="/etc/nginx/sites-available/default"
web_static_path="/data/web_static/current/"
alias_path="/hbnb_static"

if ! grep -q "$alias_path" "$nginx_config"; then
    sudo sed -i "/server_name _;/a \\\n\tlocation $alias_path {\\n\t\talias $web_static_path;\\n\t}" "$nginx_config"
fi

# Restart Nginx
sudo service nginx restart
