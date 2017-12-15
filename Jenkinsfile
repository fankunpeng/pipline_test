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
				sh 'hostname && pwd && hostname'
				sh 'ls'
			}
		}
		stage('Deploy') {
			steps {
				sh 'echo "deploy"'
			}
		}
	}
}
