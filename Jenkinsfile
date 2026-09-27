pipeline {
    agent any
    environment {
        IMAGE_NAME = "techstore/inventoryhub"
        CONTAINER_NAME = "techstore-inventory-ci"
        DB_PASSWORD = credentials("techstore-db-password")
    }
    stages {
        stage("Checkout") {
            steps { checkout scm }
        }
        stage("Install") {
            steps {
                sh "python3 -m venv .venv"
                sh ".venv/bin/pip install -r requirements.txt"
            }
        }
        stage("Tests") {
            steps { sh ".venv/bin/python -m pytest -q" }
        }
        stage("App Security") {
            steps { sh ".venv/bin/python security_check.py" }
        }
        stage("Container Policy") {
            steps { sh ".venv/bin/python container_policy.py" }
        }
        stage("Docker Build") {
            steps { sh "docker build -t \({IMAGE_NAME}:\){BUILD_NUMBER} ." }
        }
        stage("Approval") {
            steps {
                input message: "¿Promover este build a producción?", ok: "Desplegar"
            }
        }
        stage("Deploy") {
            steps {
                sh "docker rm -f ${CONTAINER_NAME} || true"
                sh "docker run -d --name \({CONTAINER_NAME} --network techstore-ci-net -p 5001:5000 -e DB_PASSWORD=\"\){DB_PASSWORD}\" \({IMAGE_NAME}:\){BUILD_NUMBER}"
            }
        }
        stage("Smoke Test") {
            steps {
                sh "sleep 2"
                sh "curl -fsS http://${CONTAINER_NAME}:5000/health"
            }
        }
    }
    post {
        always {
            sh "docker ps -a --filter name=${CONTAINER_NAME} || true"
        }
    }
}