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
				sh 'python3 -m venv env'
				sh '. env/bin/activate && hostname'
			}
		}
		stage('Deploy') {
			steps {
				sh 'echo "deploy"'
			}
		}
	}
}
