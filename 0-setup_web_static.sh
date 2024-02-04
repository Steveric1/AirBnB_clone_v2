#!/usr/bin/env bash
#Bash script that sets up your web servers for the deployment of web_static

#update and install nginx
sudo apt-get -y update
sudo apt-get -y install nginx

function configure_nginx {

    sudo mkdir -p "/data/web_static/releases/test/"
    sudo mkdir -p "/data/web_static/shared/"
    # Create a fake HTML file /data/web_static/releases/test/index.html
    echo "ALX School" | sudo tee "/data/web_static/releases/test/index.html" > /dev/null

    # Set ownership recursively to ubuntu user and group
    sudo chown -R ubuntu:ubuntu /data

    #create a symbolic link /data/web_static/current linked to the /data/web_static/releases/test/ folder
    if [ ! -L /data/web_static/current ]; then
        sudo ln -sf "/data/web_static/releases/test/" "/data/web_static/current"
    fi

    #Update the Nginx configuration to serve the content of /data/web_static/current/ to hbnb_static
    if [ -f /etc/nginx/sites-available/default ]; then
        sudo sed -i "38i \\\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}" "/etc/nginx/sites-available/default"
        #restart nginx
        sudo service nginx restart
    fi
}

#call the function
configure_nginx