pipeline {
	agent {
		docker {
			image "python"
		}
	}
	stages {
		stage('Test') {
			docker.image('python').inside {
				sh 'pwd'
    			}
				docker.image('python').inside {
					sh 'cat /etc/passwd'
				}

			steps {
				sh 'pwd'
				sh 'ls'
				sh 'cat /etc/passwd'
				sh 'uname -a'
				sh 'cat /proc/version'
				sh 'hostname'
				sh 'hostname && pwd && hostname'
				sh 'ls'
				sh 'which python3'
			}
		}
	}
}
