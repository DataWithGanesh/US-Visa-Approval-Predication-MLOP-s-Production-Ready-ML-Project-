# US-Visa-Approval-Predication-MLOP-s-Production-Ready-ML-Project-

## Tools need to be download:

- Anaconda: https://www.anaconda.com/
- Vs code: https://code.visualstudio.com/download
- Git: https://git-scm.com/
- Flowchart: https://whimsical.com/
- MLOPs Tool: https://www.evidentlyai.com/
- MongoDB: https://account.mongodb.com/account/login
- Data link: https://www.kaggle.com/datasets/moro23/easyvisa-dataset

## Project Overview

This is an end-to-end production-ready Machine Learning project that predicts US Visa approval status based on applicant features. The project demonstrates enterprise-level MLOps practices including automated pipelines, data drift monitoring, model evaluation, and cloud deployment with CI/CD integration.

### Real-World Impact

This system can be utilized by US Visa applicants to:

- Assess their approval probability before applying
- Identify areas for improvement in their application
- Optimize their resume and credentials for higher success rates
- Save time and resources by making data-driven decisions

### Problem Statement

The Immigration and Nationality Act (INA) permits foreign workers to work in the United States temporarily or permanently while protecting US workers from adverse impacts. The Office of Foreign Labor Certification (OFLC) administers these programs.

Objective
Given applicant features such as:

- continent - Geographic origin
- education - Educational qualification level
- job_experience - Years of professional experience
- training - Additional training completed
- employment - Employment details
- current - Current status
- age - Applicant's age
- And other relevant features...

Predict: Whether the visa application will be APPROVED or DENIED

### Solution Approach

#### Machine Learning Strategy

This project implements a supervised classification approach using multiple algorithms:

- Data Collection - Fetch from MongoDB Atlas
- Exploratory Data Analysis (EDA) - Understand data patterns and relationships
- Feature Engineering (FE) - Transform raw features into meaningful inputs
- Model Training - Train multiple classification algorithms
- Hyperparameter Tuning - Optimize model performance using NeuroMF
- Model Evaluation - Select best model based on performance metrics
  =- Production Deployment - Deploy via AWS with automated CI/CD

### Tech Stack

#### Core Technologies

| Category             | Technologies                                                    |
| -------------------- | --------------------------------------------------------------- |
| **Language**         | Python 3.8+                                                     |
| **ML/DL**            | Scikit-learn, Pandas, NumPy, Matplotlib, Seaborn                |
| **Database**         | MongoDB Atlas                                                   |
| **MLOps**            | Evidently AI (Drift Detection), NeuroMF (Hyperparameter Tuning) |
| **Backend**          | FastAPI                                                         |
| **Containerization** | Docker                                                          |
| **Cloud Platform**   | AWS (EC2, ECR, S3, IAM)                                         |
| **CI/CD**            | GitHub Actions                                                  |
| **Version Control**  | Git, GitHub                                                     |
| **Development**      | Jupyter Notebook, VS Code, Anaconda                             |

#### AWS Services Used

EC2: Virtual machine for hosting the application
ECR: Elastic Container Registry for Docker images
S3: Storage for production models and artifacts
IAM: Identity and Access Management for secure deployments

## Git commands

```bash
git add .

git commit -m "Updated"

git push origin main
```

## How to run?

```bash
conda create -n visa python=3.8 -y
```

```bash
conda activate visa
```

```bash
pip install -r requirements.txt
```

## Workflow:

1. constants
2. entity
3. components
4. pipeline
5. main file

## Export the environment variable

```bash

export MONGODB_URL="mongodb+srv://<username>:<password>...."

export AWS_ACCESS_KEY_ID=<AWS_ACCESS_KEY_ID>

export AWS_SECRET_ACCESS_KEY=<AWS_SECRET_ACCESS_KEY>
```
