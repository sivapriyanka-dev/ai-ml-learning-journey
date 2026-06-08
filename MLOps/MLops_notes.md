# Day 1 — Docker Fundamentals.

## What is Docker?

Docker is a platform that allows developers to automate the deployment of applications inside lightweight, portable containers. Containers are isolated environments that package an application and all its dependencies, ensuring consistency across different environments.

## Key Concepts:

1. **Container**: A lightweight, standalone, and executable package that includes everything needed to run a piece of software, including the code, runtime, system tools, libraries, and settings.
2. **Image**: A read-only template used to create containers. It contains the application and its dependencies. Images can be shared and reused across different environments.
3. **Dockerfile**: A text file that contains a series of instructions to build a Docker image. It specifies the base image, application code, dependencies, and configuration.
4. **Docker Hub**: A cloud-based registry service where users can store and share Docker images. It provides a vast repository of pre-built images for various applications and frameworks.

## Benefits of Docker:

- **Portability**: Docker containers can run on any system that supports Docker, ensuring consistency across development, testing, and production environments.
- **Isolation**: Each container runs in its own isolated environment, preventing conflicts between applications and their dependencies.
- **Scalability**: Docker allows for easy scaling of applications by running multiple containers across a cluster of machines.
- **Efficiency**: Docker containers are lightweight and start quickly, making them ideal for development and deployment.

## Docker Commands:

- `docker build`: Builds a Docker image from a Dockerfile.
- `docker run`: Runs a container from a specified image.
- `docker ps`: Lists all running containers.
- `docker stop`: Stops a running container.
- `docker rm`: Removes a stopped container.
- `docker rmi`: Removes a Docker image.
- `docker pull`: Pulls an image from a Docker registry (e.g., Docker Hub).
- `docker push`: Pushes an image to a Docker registry.

## Example Dockerfile:

```Dockerfile
# Use an official Python runtime as a base image
FROM python:3.8-slim
# Set the working directory in the container
WORKDIR /app
# Copy the current directory contents into the container at /app
COPY . /app
# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt
# Make port 80 available to the world outside this container
EXPOSE 80
# Define environment variable
ENV NAME World
# Run app.py when the container launches
CMD ["python", "app.py"]
```

This Dockerfile sets up a Python application by using a base image, copying the application code, installing dependencies, exposing a port, and defining the command to run the application.

## Conclusion:

Docker is a powerful tool for developers and DevOps teams, enabling them to create, deploy, and manage applications in a consistent and efficient manner. By understanding the fundamentals of Docker, you can streamline your development workflow and ensure that your applications run smoothly across different environments.

# Docker Terminology

Image - Blueprint - Recipe Example: python:3.11
Container - Running instance - Cake from recipe.
Dockerfile - Instructions to build image.

# my first steps

1. navigate location - cd MLOps
2. Verify - dir
3. Build Docker Image - docker build -t my-first-app .
4. Verify Image - docker images
5. Run Container - docker run my-first-app
6. See What Happened - docker ps -a

# Dockerfile and explanation on what happened

FROM python:3.11-slim
WORKDIR /app
COPY . .
CMD ["python", "app.py"]

means
Take Python image
↓
Create /app folder
↓
Copy project files
↓
Run app.py
