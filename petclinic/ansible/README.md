<br> tested on: <br>
<br> centos 8 <br>
<br>
<br>
<br> Used
<br> rename  hosts.yml.example to hosts.yml , edit credential host
<br> ansible-playbook install_base_packages.yml -v
<br>
<br> ansible-playbook setup_sonarqube.yml -v
<br>
<br> ansible-playbook setup_nginx_proxy_with_ssl.yml  --extra-vars '{"domain":"petclinic-app.domain","proxy_ip":"ip","proxy_port":"8080","email":"email@com.net"}' -v
<br>
<br>
<br> ansible-playbook setup_nginx_load_balanser.yml  --extra-vars '{"use_ssl":"True","domain":"petclinic-app.ml","proxy_ip":"ip","proxy_port":"8080","proxy_ip2":"ip","proxy_port2":"8080","email":"email@com.net"}' -v
<br>
<br> ansible-playbook setup_nginx_load_balanser.yml  --extra-vars '{"use_ssl":"False","domain":"petclinic-app.ml","proxy_ip":"ip","proxy_port":"8080","proxy_ip2":"ip","proxy_port2":"8080"}' -v
<br>
<br>
<br>
<br> ansible-playbook setup_master_slave_db.yml --tags "master" -v
<br> ansible-playbook setup_master_slave_db.yml --tags "slave" -v
<br>
<br>
<br> ansible-playbook setup_prometheus_grafana.yml -v
<br>
<br>
<br>
<br>
<br>
<br>
<br>
