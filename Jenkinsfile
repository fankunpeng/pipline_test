pipeline {
	agent any
	stages {
		stage('Test') {
			steps {
				sh 'python3 -m venv env'
				sh '. env/bin/activate'
				sh 'pip install flask'
				sh 'FLASK_APP=task.py flask run&'
			}
		}
		stage('Deploy') {
			steps {
				sh 'echo "deploy"'
			}
		}
	}
}
