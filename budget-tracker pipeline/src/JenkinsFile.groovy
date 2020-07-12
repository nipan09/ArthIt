pipeline{
	agent any
	stages
	{
	  stage('Build'){
			steps{
			  echo "Building the project.."
			  sh'''
					python3 -m pip install -r requirements.txt
                    '''
			   }
		}
		stage('Run Unit/ Integration Tests'){
			steps{
				echo "Running Unit/Integration Tests.."
				sh'''
					cd mera_project/
					python3 manage.py test
				'''
			}
		}
	}
}
