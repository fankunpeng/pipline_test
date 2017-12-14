pipeline {
	agent {
		docker {image "ubuntu"}
	}
	stages {
		stage('Test') {
			steps {
				sh 'apt update'
				sh 'apt install net-tools'
				sh 'ifconfig'
				sh 'pwd'
				sh 'apt install python3 && python3 -m venv env && . env/bin/activate && which python && pip install flask &&  FLASK_APP=task.py flask run && sleep 5000'
			}
		}
		stage('Deploy') {
			steps {
				sh 'echo "deploy"'
			}
		}
	}
}
