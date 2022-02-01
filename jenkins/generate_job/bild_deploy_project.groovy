job('build_deploy_project') {
  logRotator {
    numToKeep(2)
  }
  parameters {
    textParam ( 'REMOTE_DIRECTORY' , '/opt/petclinic/' , '' )
    textParam ( 'REMOTE_PREFIX' , 'target/' , '' )
    textParam ( 'PROJECT_FILE_NEW' , 'spring-petclinic-2.5.0-SNAPSHOT.jar' , '' )
  }

  scm {
    git{
      remote {
        name('main')
        url('https://gogs-repo.ml/git/kondratenko/spring-petclinic.git')
      }
      branch 'main'
    }
  }

  triggers {
    scm ''
  }
  steps {
    shell("./mvnw package")
  }

  steps {
     shell("echo \"REMOTE_PREFIX: \${REMOTE_PREFIX}\" ; echo \"PROJECT_FILE_NEW:  \${PROJECT_FILE_NEW}\" ; echo \"REMOTE_DIRECTORY: \${REMOTE_DIRECTORY}\"")
  }
  steps {
    remoteShell('user@ip:22') {
      command('sudo mkdir -p \${REMOTE_DIRECTORY} ; sudo chown ec2-user:ec2-user --recursive \${REMOTE_DIRECTORY}')
    }
    publishOverSsh {
      server('da-kondrate-app') {
        transferSet {
          removePrefix("\${REMOTE_PREFIX}")
          sourceFiles('\${REMOTE_PREFIX}\${PROJECT_FILE_NEW}')
          remoteDirectory('\${REMOTE_DIRECTORY}')
          execCommand('ls -la  \${REMOTE_DIRECTORY}\${PROJECT_FILE_NEW}')

        }
      }
    }


  }
  steps {
  	remoteShell('user@ip:22') {
      command('''
sudo touch /etc/systemd/system/petclinic.service
sudo chmod 777 /etc/systemd/system/petclinic.service
sudo echo \"[Unit]
Description=Manage java application spring-petclinic

[Service]
WorkingDirectory=\${REMOTE_DIRECTORY}
ExecStart=/usr/bin/java -jar \${REMOTE_DIRECTORY}\${PROJECT_FILE_NEW}
ExecStop=/bin/kill -15 \\\$MAINPID
User=apprunner
Type=simple
Restart=on-failure
RestartSec=60

[Install]
WantedBy=multi-user.target
\" > /etc/systemd/system/petclinic.service
sudo chmod 664 /etc/systemd/system/petclinic.service

''')
      command('sudo grep -q "^apprunner:" /etc/passwd && echo exists || sudo adduser apprunner')
      command('sudo chown apprunner:apprunner --recursive \${REMOTE_DIRECTORY}')
      command('sudo systemctl daemon-reload')
      command('sudo systemctl restart petclinic')
      command('sudo systemctl enable  petclinic')
    }

  }

}
