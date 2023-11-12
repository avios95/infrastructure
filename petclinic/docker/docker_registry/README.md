--------------------------------------------------------------------------------
Create passwords file

sudo mkdir -p /opt/docker_registry/auth/; sudo docker run --entrypoint htpasswd registry:2.7.0 -Bbn user password12345 >> /opt/docker_registry/auth/.htpasswd

--------------------------------------------------------------------------------
Generate cert

sudo certbot certonly --manual --preferred-challenges dns -i nginx --manual-public-ip-logging-ok --agree-tos --no-eff-email -m email@com.net -d {{ NGINX_HOST }}

Then edit DNS zone

--------------------------------------------------------------------------------
Start containers

sudo docker-compose up -d

--------------------------------------------------------------------------------
After 3 month
sudo certbot renew ; sudo docker-compose restart
