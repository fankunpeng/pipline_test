pipeline {
	agent {
		docker {image "python"}
	}
	stages {
		stage('Test') {
			steps {
				sh 'hostname'
				sh 'pwd'
			}
		}
		stage('Deploy') {
			steps {
				sh 'echo "deploy"'
			}
		}
	}
}
