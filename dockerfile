# Use the official Python image with version 3.10
FROM python:3.10

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt /app/

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code into the container
COPY . /app/

# Set environment variables from .env file
ARG ENV_FILE
ENV ENV_FILE=${ENV_FILE:-.env}
COPY $ENV_FILE /app/.env

# Command to run your application
CMD ["python", "main.py"]
