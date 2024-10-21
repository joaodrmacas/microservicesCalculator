# Use an official Python runtime as the base image
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /app

# Install curl and required packages
RUN apt-get update && apt-get install -y curl && apt-get install -y nano && apt install netcat-traditional -y && apt install inetutils-ping -y && apt install dnsutils -y && apt-get clean

# Copy the current directory contents into the container at /app
COPY . /app

# Install Flask
RUN pip install Flask

# Install Requests
RUN pip install Requests

# Make port 5000 available to the world outside this container
EXPOSE 5000

# Define environment variable to avoid buffering
ENV PYTHONUNBUFFERED=1

# Run the Flask app
CMD ["python", "app.py"]
