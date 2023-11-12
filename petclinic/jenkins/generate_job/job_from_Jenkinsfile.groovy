pipelineJob('build_deploy_on_Dockerfile') {
  logRotator {
    numToKeep(2)
  }

  definition {

    cpsScm{
      scm {
        git{
          remote {
            name('main')
            url('https://gogs-repo.ml/git/kondratenko/spring-petclinic.git')
          }
          branch 'main'
        }
      }
      scriptPath('Jenkins/job/petclinic_build_deploy_on_Dockerfile/Jenkinsfile')
    }
  }
}
pipelineJob('build_deploy_app_use_node_agent') {
  logRotator {
    numToKeep(2)
  }

  definition {

    cpsScm{
      scm {
        git{
          remote {
            name('main')
            url('https://gogs-repo.ml/git/kondratenko/spring-petclinic.git')
          }
          branch 'main'
        }
      }
      scriptPath('Jenkins/job/petclinic_build_deploy_app_use_node_agent/Jenkinsfile')
    }
  }
}
pipelineJob('build_deploy_with_sqlite') {
  logRotator {
    numToKeep(2)
  }

  definition {

    cpsScm{
      scm {
        git{
          remote {
            name('main')
            url('https://gogs-repo.ml/git/kondratenko/spring-petclinic.git')
          }
          branch 'main'
        }
      }
      scriptPath('Jenkins/job/petclinic_include_pipeline_sqlite/Jenkinsfile')
    }
  }
}
pipelineJob('build_deploy_with_local_docker_db') {
  logRotator {
    numToKeep(2)
  }

  definition {

    cpsScm{
      scm {
        git{
          remote {
            name('main')
            url('https://gogs-repo.ml/git/kondratenko/spring-petclinic.git')
          }
          branch 'main'
        }
      }
      scriptPath('Jenkins/job/petclinic_include_pipeline_local_docker_db/Jenkinsfile')
    }
  }
}
pipelineJob('build_deploy_with_remote_server_db') {
  logRotator {
    numToKeep(2)
  }

  definition {

    cpsScm{
      scm {
        git{
          remote {
            name('main')
            url('https://gogs-repo.ml/git/kondratenko/spring-petclinic.git')
          }
          branch 'main'
        }
      }
      scriptPath('Jenkins/job/petclinic_include_pipeline_remote_server_db/Jenkinsfile')
    }
  }
}
