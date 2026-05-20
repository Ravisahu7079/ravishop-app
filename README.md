# ravishop-app

# 🛒 RaviShop -- Cloud-Native E-Commerce REST API

![Python](https://img.shields.io/badge/Python-3.12-blue)
![Flask](https://img.shields.io/badge/Flask-3.0-green)
![Docker](https://img.shields.io/badge/Docker-Containerized-blue)
![Kubernetes](https://img.shields.io/badge/Kubernetes-K8s-blue)
![CI/CD](https://img.shields.io/badge/CI%2FCD-GitHub%20Actions-green)
![AWS](https://img.shields.io/badge/AWS-Cloud-orange)


## 📌 Project Overview

RaviShopp is a production-grade, cloud-native REST API built with Python Flask.
This Project demonstrates a complete DevOps lifecycle - from code to cloud.

## ✨ Features

- REST API with CRUD operations
- Containerized with Docker
- Kubernetes deployment with auto-scaling
- CI/CD pipeline ( lint, test, security scan )
- GitOps  with Argo CD
- Infrastructure as Code ( Terraform )
- Monitoring with Prometheus + Grafana
- AWS Cloud deployment ready

## 🏗️  Architecture

![Architecture](RaviShop%20Diagram.drawio.png)

    Developer
    ↓
    Git Push → GitHub
    ↓
    GitHub Actions CI/CD Pipeline
    |—————Lint ( flake8 )
    |—————Unit Tests ( pytest )
    |—————Security Scan ( Trivy )
    |—————Docker Build + Push to ECR
    ↓
    Argo CD ( GitOps ) watches ravishop-k8s repo
    ↓
    Kubernetes Cluster ( k3s/AWS EKS )
    |—————Deployment ( 2 replicas )
    |—————Service ( NodePort )
    |—————Ingress
    ↓
    AWS Infrastructure ( Terraform )
    |—————VPC ( public + private subnets )
    |—————EC2 ( t3.micro )
    |—————RDS MySQL ( db.t3.micro )
    ↓
    Monitoring
    |—————Prometheus ( metrics )
    |—————Grafana ( dashboard )
    |—————CloudWatch ( AWS alrm )


## 🚀 Tech Stack

| Category | Technology |
|---|---|
| Backend | Python 3.12, Python Flask 3.0, SQLALchemy |
| Database | MySQL (AWS RDS) / SQLite (local) |
| Container | Docker, AWS ECR |
| Orchestration | Kubernetes (k3s / AWS EKS) |
| IaC | Terraform |
| Config Mgmt | Ansible |
| CI/CD | GitHub Actions |
| GitOps | Argo CD |
| Monitoring | Prometheus, Grafana, CloudWatch |
| Cloud | AWS (VPC, EC2, RDS, S3, ECR, IAM) |


## 📁 Related Repositories

     https://github.com/Ravisahu7079/

| Repo | Description |
|---|---|
| ravishop-app/    | Flask API + Docker + CI/CD |
| ravishop-infra/  | Terraform + Ansible |
| ravishop-k8s/    | Kubernetes + Argo CD |


## 🔌  API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | /health | Health check |
| GET | /products | List all products |
| POST | /products | Create product |
| GET | /products/:id | Get product |
| PUT | /products/:id | Update product |
| DELETE | /products/:id | Delete product |


## 🛠️  Local Setup

```bash
    # Clone repo
    git clone https://github.com/Ravisahu7079/ravishop-app.git
    cd ravishop-app

    # Virtual environment
    Python3 -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt

    # Run app
    Python3 run.py
```

## 🐳  Docker Setup

```bash
    docker build -t ravishop:v1 .
    docker run -d -p 5000:5000 --env-file .env ravishop:v1
    curl http://localhost:5000/health
```
## ☸️ Kubernetes Deploy

```bash
    kubectl apply -f manifests/base/
    curl http://localhost:32099/health
```
## ♾️  CI/CD Pipeline

    Code Push to main branch triggers:

    1. Lint check ( flake8 )
    2. Unit Tests ( pytest ) - 5 tests
    3. Security Scan ( Trivy )
    4. Docker Build + Version Tag
    5. Push to AWS ECR


## 📊  Monitoring

    • Prometheus — metrics collection from app + nodes
    • Grafana    — Node Exporter Full dashboard ( ID:1860 )
    • CloudWatch — CPU/Memory alerts on AWS


## 🧑‍💻  Author

    Ravi Sahu

    • GitHub: @Ravisahu7079
    • Role: DevOps/Cloud engineer

## 📄 License

    MIT License































