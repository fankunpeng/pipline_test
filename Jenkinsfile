pipeline {
    agent none 
    stages {
        stage('Build') { 
            agent {
                docker {
                    image 'python' 
                }
            }
            steps {
                sh 'g++ hello.cpp'
                sh 'pip install flask'
            }
        }
    }
}
