#!/usr/bin/env bash
# This script sets up webservers for the deployment of the webstatic

# Update and install nginx if it doesnt exist
apt-get -y update
apt-get -y install nginx

function server_config {
    # Create the directories if they dont exist
    mkdir -p "/data/web_static/releases/test/"
    mkdir -p "/data/web_static/shared/"

    # Create a fake html file
    echo -e "<html>\n\t<head>\n\t</head>\n\t<body>\n\t\t<h1>Hello ALX</h1>\n\t</body>\n</html>" > /data/web_static/releases/test/index.html
    # Set ownership of the directories
    chown -R ubuntu:ubuntu /data/
    # Create a symbolic link
    ln -sf "/data/web_static/releases/test/" "/data/web_static/current"
    # Update the nginx configuration
    sed -i "38i location /hbnb_static/ {\n\talias /data/web_static/current/;\n}" "/etc/nginx/sites-available/default"
    # Restart the nginx service
    service nginx restart
}

# Call the function
server_config