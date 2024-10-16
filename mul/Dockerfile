# Use an official Node.js image as the base image
FROM node:14

# Set the working directory inside the container
WORKDIR /app

# Copy package.json and install dependencies
COPY package*.json ./
RUN npm install

# Copy the rest of the application
COPY . .

# Expose port 5000 for the multiplication service
EXPOSE 5000

# Run the Node.js server
CMD ["node", "mul.js"]
