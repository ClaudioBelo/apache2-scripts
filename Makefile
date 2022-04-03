install:
	sudo apt-get update
	sudo apt-get install apache2 -y
	sudo service apache2 start
	sudo a2enmod proxy
	sudo a2enmod proxy_http
	sudo service apache2 restart

add-vhost:
	sudo python scripts/add_host.py
	