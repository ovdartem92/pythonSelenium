agent { label 'python39' }
  options { timeout(time: 20, unit: 'MINUTES') }
      stage('Install Dependencies') {
      steps {
        sh """
          python -m venv .env
          source ./.env/bin/activate
          python -m pip install -r requirements.txt
          """
      }
    }