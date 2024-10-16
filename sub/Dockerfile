# Use an official Golang image as the base image
FROM golang:1.17-alpine

# Set the working directory inside the container
WORKDIR /app

# Copy the Go code into the container
COPY . .

# Build the Go binary
RUN go mod init sub

RUN go build -o sub .

# Expose port 5000 for the subtraction service
EXPOSE 5000

# Run the Go binary
CMD ["./sub"]
