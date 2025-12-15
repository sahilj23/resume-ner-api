# Resume NER API

Note: This repository focuses on model inference and deployment; the full preprocessing, training, and evaluation pipeline is documented in the original project repository: [https://github.com/sahilj23/resume-ner-model-training]

A production‑ready Resume Information Extraction API built using FastAPI, Hugging Face Transformers, Docker, and GitHub Actions (CI).
The service performs Named Entity Recognition (NER) on resume text to extract structured work‑experience information such as role, company, start date, and end date.

This project focuses on clean ML inference, API design, and industry‑standard deployment practices, rather than model experimentation alone.

## Problem Statement

Recruitment systems often receive resumes in unstructured text form, making automated parsing and analysis difficult.

This project solves that by:

Converting raw resume text into structured entities

Exposing the model via a REST API

Packaging the service using Docker

Validating builds automatically using CI

Test-deploying the service on Google Cloud Run


## *** Key Features *** 

Fine‑tuned BERT‑based NER model for resume text

FastAPI backend with schema validation

Clean separation of inference logic and API layer

Dockerized for reproducible builds

GitHub Actions CI to automatically build Docker image on every push

Extracted Entities

The model predicts the following entities:

ROLE

COMPANY

START_DATE

# *** API Endpoints *** 

Health Check  -- GET /health
Extract Resume Entities -- POST /extract-entities

Request Body  -- {
"text": "Worked as a Data Analyst at Top Trove Foundation from Jan 2021 to Dec 2023"
}

Response -- {
"entities": {
"ROLE": ["Data Analyst"],
"COMPANY": ["Top Trove Foundation"],
"START_DATE": [],
"END_DATE": []
}
}

Running Locally (Without Docker)
pip install -r requirements.txt
uvicorn app.main:app --reload


Open:

http://127.0.0.1:8000/docs

Running with Docker
docker build -t resume-ner-api .
docker run -p 8000:8000 resume-ner-api


Swagger UI:

http://localhost:8000/docs



## *** Tech Stack ***

Python 3.10

FastAPI – API framework

Hugging Face Transformers – Model inference

PyTorch – Backend ML framework

Docker – Containerization

GitHub Actions – CI pipeline

Google Cloud Run (test deployment)


## *** CI/CD Overview ***

This repository includes a GitHub Actions workflow that:

Triggers on every push or pull request to main

Builds the Docker image using Buildx

Fails fast if the application or Docker build breaks

This ensures code changes are continuously validated before deployment.
END_DATE

If an entity is not confidently detected, the API explicitly returns an empty list, ensuring transparency.

## *** Cloud Deployment (Google Cloud Run) ***

The Dockerized service was test-deployed on Google Cloud Run to validate:

Container compatibility

Runtime configuration

API accessibility in a managed cloud environment

The service was later decommissioned after validation due to billing constraints, as this is a personal project.
The setup remains fully reproducible and cloud-ready.

