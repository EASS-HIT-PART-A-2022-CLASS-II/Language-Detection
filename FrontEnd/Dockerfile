# Dockerfile for Frontend service
FROM python:3.9

COPY requirements.txt app/requirements.txt

WORKDIR /app

# Install the required packages
RUN apt-get update && apt-get install -y \
    postgresql-client \
    && rm -rf /var/lib/apt/lists/*

# Install the Python packages from requirements.txt
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install pytest

# Set the environment variable for the PostgreSQL host
ENV PGHOST=postgres

COPY . /app

EXPOSE 8501

ENTRYPOINT ["streamlit","run"]
CMD ["app.py"]
