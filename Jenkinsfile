pipeline {
	agent {
		docker {
			image "python"
		}
	}
	stages {
		stage('Test') {
			steps {
				sh 'pwd'
				sh 'ls'
				sh 'hostname'
			}
		}
		stage('Deploy') {
			steps {
				sh 'echo "deploy"'
			}
		}
	}
}
