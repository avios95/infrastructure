Install certbot:\
https://tecadmin.net/how-to-install-certbot-on-centos-8/
```
sudo dnf install https://dl.fedoraproject.org/pub/epel/epel-release-latest-8.noarch.rpm
sudo dnf install certbot python3-certbot-nginx
```

--------------------------------------------------------------------------------
Generate cert

`
sudo certbot certonly --manual --preferred-challenges dns -i nginx --manual-public-ip-logging-ok --agree-tos --no-eff-email -m mail@com.net -d {{ NGINX_HOST }}
`

Then edit DNS zone

--------------------------------------------------------------------------------
create `$PWD/nginxconfig/petclinic-app.ml.conf.template`

--------------------------------------------------------------------------------
Start containers
```
docker stop nginx-app &&  docker rm nginx-app || echo 'nginx-app is not running';
docker run -d --name nginx-app --restart always \
            -e NGINX_HOST=petclinic-app.ml \
            -e PROXY_ADDRESS=java-petclinic \
            -e PROXY_PORT=8080 \
            -p 80:80 -p 443:443 \
            --link java-petclinic:java-petclinic \
            -v $PWD/nginxconfig:/etc/nginx/templates \
            -v /etc/letsencrypt:/etc/letsencrypt  nginx
```


--------------------------------------------------------------------------------
check https://petclinic-app.ml/

--------------------------------------------------------------------------------
After 3 month

`sudo certbot renew ; sudo service docker restart`
