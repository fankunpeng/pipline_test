pipeline {
	agent any
	stages {
		stage('Test') {
		agent {
			docker {
				image "python"
			}
			}

			steps {
				docker.image('python').inside{
					sh 'pwd'
				}
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
