pipeline {
	agent {
		docker {image "python"}
	}
	stages {
		stage('Test') {
			steps {
				sh 
				sh 'python3 -m venv env && . env/bin/activate && which python && pip install flask &&  FLASK_APP=task.py flask run && sleep 5000'
			}
		}
		stage('Deploy') {
			steps {
				sh 'echo "deploy"'
			}
		}
	}
}
