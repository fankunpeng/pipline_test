pipeline {
	agent {
		any
	}
	stages {
		stage('Test') {
			steps {
				sh 'g++ hello.cpp'
         			sh './a.out'
				sh 'pwd'
				sh 'hostname'
			}
		}
	}
}
