pipeline {
	agent {
		docker {image "python"}
	}
	stages {
		stage('Test') {
			steps {
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
