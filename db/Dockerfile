# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /db

# Copy the current directory contents into the container at /app
COPY . /db

# Install any needed packages specified in requirements.txt
RUN pip install Flask pymongo

# Make port 5000 available to the world outside this container
EXPOSE 5000

# Define environment variable to ensure output is shown immediately (useful for logging)
ENV PYTHONUNBUFFERED=1

# Run the Flask app when the container launches
CMD ["python", "db.py"]
