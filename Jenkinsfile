pipeline {
	
	stages {
		stage('Test') {
		agent {
			docker {
				image "python"
			}
			}

			steps {
				sh 'pwd'
				sh 'ls'
				sh 'hostname'
				sh 'hostname && pwd && hostname'
				sh 'ls'
			}
		}
	}
}
