pipeline {
   agent none
   stages {
       stage('test') {
           agent {
	       docker {
	           image 'python'
		}
		steps {
		    sh 'gcc -v'
		    sh 'pwd'
		}
	}
    }
}
}
