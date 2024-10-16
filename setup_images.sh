#!/bin/bash

# Function to build a Docker image for a given service
build_image() {
    service_name=$1
    docker_image_tag=$2

    echo "Building Docker image for $service_name..."

    # Navigate to the service's directory
    cd $service_name || exit

    # Build the Docker image
    docker build -t $docker_image_tag .

    # Navigate back to the root directory
    cd ..

}

# Build the Docker images for each service
build_image "sum" "sum-service:latest"
build_image "sub" "sub-service:latest"
build_image "mul" "mul-service:latest"
build_image "div" "div-service:latest"

echo "All Docker images built successfully!"