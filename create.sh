sudo unzip latest.zip -d /usr/share/nginx/

sudo mv /usr/share/nginx/wordpress /usr/share/nginx/$1

cd /usr/share/nginx/$1/

sudo cp wp-config-sample.php wp-config.php

sudo chown www-data:www-data /usr/share/nginx/$1/ -R

sudo /etc/nginx/conf.d/$1.conf > $2
