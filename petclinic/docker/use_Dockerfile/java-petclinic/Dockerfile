FROM openjdk:11
RUN apt-get update -y && apt-get upgrade -y&& apt-get install git -y
RUN mkdir -p /opt/petclinic; cd /opt/petclinic; git clone https://github.com/spring-projects/spring-petclinic.git
WORKDIR /opt/petclinic/spring-petclinic
RUN  sed -i "s#localhost#mysql-petclinic#g" src/main/resources/application-mysql.properties; ./mvnw package
EXPOSE 8080
ENTRYPOINT java -Dspring.profiles.active=mysql -jar ./target/*.jar > /opt/petclinic/logs/java.log
