# lightweight Python base image
FROM python:3.10-slim

# working directory inside container
WORKDIR /app

# installing system dependencies for torch
RUN apt-get update && apt-get install -y \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# requirements
COPY requirements.txt .

# installing Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# copying application code
COPY app ./app
COPY resume_ner_model ./resume_ner_model

# FastAPI port
EXPOSE 8000

# running FastAPI with Uvicorn
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
