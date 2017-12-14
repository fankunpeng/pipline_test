pipeline {
	agent {
		docker {image "ubuntu"}
	}
	stages {
		stage('Test') {
			steps {
				sh 'python3 -m venv env'
				sh 'apt update'
				sh 'apt install net-tools'
				sh 'ifconfig'
				sh '. env/bin/activate && which python && pip install flask &&  FLASK_APP=task.py flask run && sleep 5000'
			}
		}
		stage('Deploy') {
			steps {
				sh 'echo "deploy"'
			}
		}
	}
}
