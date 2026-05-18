# ravishop-app

# RaviShop -- Cloud-Native E-Commerce REST API

![Python](https://img.shields.io/badge/Python-3.12-blue)


![Flask](https://img.shields.io/badge/Flask-3.0-green)


![Docker](https://img.shields.io/badge/Docker-Containerized-blue)


![Kubernetes](https://img.shields.io/badge/Kubernetes-K8s-blue)


![CI/CD](https://img.shields.io/badge/CI%2FCD-GitHub%20Actions-green)


![AWS](https://img.shields.io/badge/AWS-Cloud-orange)



##   Project Overview

RaviShopp is a production-grade, cloud-native REST API built with Python Flask.
This Project demonstrates a complete DevOps lifecycle - from code to cloud.


##   Architecture

Developer --> Git Push --> GitHub Actions CI/CD

|

Lint --> Test --> Trivy Scan

|

Docker Build --> ECR Push

|

Argo CD (GitOps) --> K8s Deploy

|

Prometheus + Grafana + CloudWatch



##  Tech Stack

| Category | Technology |
|---|---|
| Backend | Python Flask, SQLALchemy |
| Database | MySQL (AWS RDS) / SQLite (local) |
| Container | Docker, AWS ECR |
| Orchestration | Kubernetes (k3s / AWS EKS) |
| IaC | Terraform |
| Config Mgmt | Ansible |
| CI/CD | GitHub Actions |
| GitOps | Argo CD |
| Monitoring | Prometheus, Grafana, CloudWatch |
| Cloud | AWS (VPC, EC2, RDS, S3, ECR, IAM) |


##  Repository Structure

ravishop-app/    --> Flask API + Docker + CI/CD
ravishop-infra/  --> Terraform + Ansible
ravishop-k8s/    --> Kubernetes + Argo CD


##   API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| Get | /health | Health check |
| Get | /products | List all products |
| POST | /products | Create product |
| Get | /products/:id | Get product |
| Get | /products/:id | Update product |
| DELETE | /products/:id | Delete product |


##   Local Setup

```bash
# Clone repo
git clone https://github.com/Ravisahu7079/ravishop-app.git
cd ravishop-app


# Setup virtual environment
Python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# Run app
Python3 run.py
```

##   Docker Setup

```bash
docker build -t ravishop:v1 .
docker run -d -p 5000:5000 --env-file .env ravishop:v1
```

##   CI/CD Pipeline

Push to main branch triggers:

1. Lint (flake8)
2. Unit Tests (pytest)
3. Security Scan (Trivy)
4. Docker Build + Tag
5. Push to AWS ECR


##   Monitoring

- Prometheus metrics collection
- Grafana dashboards(Node Exporter Full-ID 1860)
- CloudddWatch alarms for CPU/Memory


##   Author

Ravi Sahu

  - GitHub: @Ravisahu7079
  - Role: DevOps/Cloud engineer

##  License

MIT License































