### Resume NER API

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


## *** Tech Stack ***

Python 3.10

FastAPI – API framework

Hugging Face Transformers – Model inference

PyTorch – Backend ML framework

Docker – Containerization

GitHub Actions – CI pipeline

## *** CI/CD Overview ***

This repository includes a GitHub Actions workflow that:

Triggers on every push or pull request to main

Builds the Docker image using Buildx

Fails fast if the application or Docker build breaks

This ensures code changes are continuously validated before deployment.
END_DATE

If an entity is not confidently detected, the API explicitly returns an empty list, ensuring transparency.
