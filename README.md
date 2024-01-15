# Fyle Backend Challenge

## Introduction

This project is part of the Fyle Backend Challenge and is designed for candidates who wish to intern at Fyle. It involves writing a backend service for a classroom management system.

## Getting Started

### Prerequisites

- Python 3.8
- Virtualenv
- Docker (optional, for containerization)

### Installation

1. Fork and clone the repository:

```bash
git clone https://github.com/Supreethsk05/fyle-interview-intern-backend.git
cd fyle-interview-intern-backend
Create and activate a virtual environment:
bash
Copy code
virtualenv env --python=python3.8
source env/bin/activate
Install the requirements:
bash
Copy code
pip install -r requirements.txt
Database Setup
Reset and upgrade the database using Flask-Migrate:

bash
Copy code
export FLASK_APP=core/server.py
rm -f core/store.sqlite3
flask db upgrade -d core/migrations/
Running the Server
Start the server using the provided script:

bash
Copy code
bash run.sh
Running Tests
Run tests and generate a coverage report:

bash
Copy code
pytest -vvv -s tests/
To view the test coverage report:

bash
Copy code
pytest --cov
open htmlcov/index.html
Dockerization (Optional)
To containerize the application using Docker, follow these steps:

Create a Dockerfile in the project root:
Dockerfile
Copy code
# Use an official Python runtime as a parent image
FROM python:3.8

# Set the working directory in the container
WORKDIR /usr/src/app

# Copy the current directory contents into the container at /usr/src/app
COPY . .

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Make port 5000 available to the world outside this container
EXPOSE 5000

# Define environment variable
ENV FLASK_APP=core/server.py

# Run run.sh when the container launches
CMD ["bash", "run.sh"]
Create a docker-compose.yml file:
yaml
Copy code
version: '3'
services:
  web:
    build: .
    ports:
      - "5000:5000"
    volumes:
      - .:/usr/src/app
    environment:
      - FLASK_APP=core/server.py
Build and run the application using Docker Compose:
bash
Copy code
docker-compose up --build
This will start the Flask server within a Docker container, accessible at http://localhost:5000.

Additional Information
For more detailed instructions, troubleshooting, and additional functionalities, refer to the documentation provided in Application.md.
If you encounter any issues or have questions, please reach out via the email provided or create an issue in the GitHub repository.