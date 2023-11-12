sudo docker network create network_petclinic

--------------------------------------------
cd mysql-petclinic

sudo docker build -t mysql-petclinic .

sudo docker run -d --rm --name mysql-petclinic -p 3306:3306 -v /opt/petclinic/mysql:/var/lib/mysql --network network_petclinic mysql-petclinic

--------------------------------------------
cd java-petclinic

sudo docker build -t java-petclinic .

sudo docker run -d --rm --name java-petclinic  -p 80:8080 -v /opt/petclinic/logs:/opt/petclinic/logs --network network_petclinic java-petclinic
