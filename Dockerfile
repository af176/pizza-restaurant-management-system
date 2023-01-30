# Use an official Python image as the base image
FROM python:3.9-alpine

# Set the working directory in the container
WORKDIR /app

# Copy the required files to the container
COPY . .

# Install the required packages
RUN pip install -r requirements.txt

# Use official MongoDB image
FROM mongo:4.4.3-bionic

# Expose the default MongoDB port
EXPOSE 27017

# Run the MongoDB service in the background
CMD [ "mongod" ]
