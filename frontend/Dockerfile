# Use an official Node.js runtime as the base image
FROM node:18

# Set the working directory in the container
WORKDIR /app

# Copy the package.json and package-lock.json to the container
COPY package.json .
COPY package-lock.json .

# Install project dependencies
RUN npm install

# Copy the rest of your application's source code to the container
COPY . .

# Expose the port your application will listen on
EXPOSE 3000

# Define the command to run your Node.js application
CMD ["npm", "start"]