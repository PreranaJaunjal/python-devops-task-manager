
# Python Task Manager API

## Project Overview

Python Task Manager is a REST API application
developed using Python and FastAPI.

It allows users to create, view, update and
delete tasks.

## Application Features

- Create a task
- View all tasks
- Get a task by ID
- Update an existing task
- Delete a task
- Application health check
- Automated test cases

## Technology Stack

- Python
- FastAPI
- Uvicorn
- Pytest
- HTTPX
- Git and GitHub

## Project Structure

app/       - Application source code
tests/     - Automated test cases
README.md  - Project documentation
requirements.txt - Dependencies

## Installation

Clone the repository:

git clone YOUR_GITHUB_REPOSITORY_URL

Navigate to the project:

cd python-devops-task-manager

Create virtual environment:

python -m venv venv

Activate on Windows:

.\venv\Scripts\activate

Install dependencies:

python -m pip install -r requirements.txt

## Run Application

uvicorn app.main:app --reload

## API Documentation

http://127.0.0.1:8000/docs

## Health Check

http://127.0.0.1:8000/health

## Run Automated Tests

python -m pytest -v

## Future DevOps Implementation

- GitHub integration
- Docker containerization
- Jenkins CI/CD pipeline
- AWS ECR
- AWS EKS
- Kubernetes deployment
- Terraform infrastructure
- Prometheus and Grafana monitoring
