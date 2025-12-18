# Dockerized Inference Environment

## Overview
This project demonstrates a Dockerized Machine Learning inference API using FastAPI.
The application is containerized using Docker and deployed on AWS EC2.

### Tech Stack
- Python 3.10
- FastAPI
- Docker
- GitHub Actions (CI/CD)
- DockerHub
- AWS EC2

#### How to Run the Project

# Prerequisites
- Docker installed
- Internet connection1

## Build Docker Image
```bash
docker build -t inference-api .

##### Deployment
```bash
The application is deployed on AWS EC2 and is publicly accessible.

- Live API URL: http://13.203.231.64
- Swagger UI: http://13.203.231.64/docs

###### CI/CD Pipeline
```bash
This project implements a Continuous Integration and Continuous Deployment (CI/CD) pipeline using GitHub Actions.

# CI/CD Workflow
```bash
- On every push to the `main` branch:
  - The source code is checked out
  - Dependencies are installed
  - Unit tests are executed
  - A Docker image is built
  - The Docker image is pushed to DockerHub automatically

This automation ensures consistent, reliable, and reproducible deployments of the inference service.
