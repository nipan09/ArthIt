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
		stage('Collect Static files')
		{
			steps
			{
				echo "Collecting static files.."
				cd mera_project/
				sh'''
					python3 manage.py collectstatic --noinput
				'''
			}
		}
		stage('Run Unit/ Integration Tests'){
			steps{
				echo "Running Unit/Integration Tests.."
				cd mera_project/
				sh'''
					python3 manage.py test
				'''
			}
		}
	}
}
