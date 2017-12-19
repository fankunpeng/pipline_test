node {
    checkout scm
    def customImage = docker.build("flask_app:${env.BUILD_ID}")
    customImage.inside {
        sh 'hostname'
        }
    }

