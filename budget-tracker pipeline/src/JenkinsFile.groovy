pipeline{
	agent any
	stages
	{
	  stage('Build'){
			steps{
			  echo "Building the project.."
			  sh'''
					pip3 install -r requirements.txt
                    '''
			   }
		}
		stage('Collect Static files')
		{
			steps
			{
				echo "Collecting static files.."
				sh'''
					python3 manage.py collectstatic --noinput
				'''
			}
		}
		stage('Run Unit/ Integration Tests'){
			steps{
				echo "Running Unit/Integration Tests.."
				sh'''
					python3 manage.py test
				'''
			}
		}
	}
}
