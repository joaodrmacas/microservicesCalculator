# Use an official Python runtime as the base image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install Flask
RUN pip install Flask requests

# Make the port 5000 available to the world outside this container
EXPOSE 5000

# Define environment variable to avoid buffering
ENV PYTHONUNBUFFERED=1

# Run the application
CMD ["python", "sum.py"]
