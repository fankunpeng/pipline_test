pipeline {
	agent any
	stages {
		stage('Test') {
			steps {
				sh 'python3 -m venv env'
				sh '. env/bin/activate'
				sh 'which python'
				sh 'pip install flask'
				sh 'FLASK_APP=task.py flask run&'
				sh 'sleep 5000'
			}
		}
		stage('Deploy') {
			steps {
				sh 'echo "deploy"'
			}
		}
	}
}
