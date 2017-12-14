pipeline {
	agent {
		docker {image "ubuntu"}
	}
	stages {
		stage('Test') {
			steps {
				sh  '. env/bin/activate && which python && pip install flask &&  FLASK_APP=task.py flask run && sleep 5000'
			}
		}
		stage('Deploy') {
			steps {
				sh 'echo "deploy"'
			}
		}
	}
}
