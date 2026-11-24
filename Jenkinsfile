pipeline {
  agent any
  stages {
    stage('Checkout') { steps { checkout scm } }
    stage('Build')    { steps { sh 'docker build -t proyecto_web:${BUILD_NUMBER} ./app' } }
    stage('Test')     { steps { sh 'docker run --rm proyecto_web:${BUILD_NUMBER} python -m py_compile app.py' } }
  }
}