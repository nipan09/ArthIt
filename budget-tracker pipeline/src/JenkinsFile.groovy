pipeline{
	agent any
	stages
	{
	  stage('Build'){
			steps{
			  echo "Building the project..."
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
	post{
		success{
			emailext (
				subject: "SUCCESSFUL: Job '${env.JOB_NAME} [${env.BUILD_NUMBER}]'",
				body: """<p>SUCCESSFUL: Job '${env.JOB_NAME} [${env.BUILD_NUMBER}]':</p>
            <p>Check console output at &QUOT;<a href='${env.BUILD_URL}'>${env.JOB_NAME} [${env.BUILD_NUMBER}]</a>&QUOT;</p>""",
				recipientProviders: [[$class: 'DevelopersRecipientProvider']]
			  )
		}
		failure{
			emailext (
				subject: "FAILED: Job '${env.JOB_NAME} [${env.BUILD_NUMBER}]'",
				body: """<p>FAILED: Job '${env.JOB_NAME} [${env.BUILD_NUMBER}]':</p>
            <p>Check console output at &QUOT;<a href='${env.BUILD_URL}'>${env.JOB_NAME} [${env.BUILD_NUMBER}]</a>&QUOT;</p>""",
				recipientProviders: [[$class: 'DevelopersRecipientProvider']]
				)
		}
	}
}
