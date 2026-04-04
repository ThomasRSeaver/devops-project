# Operations (Docker Setup)

## Overview

This folder contains the Docker configuration used to run the application in a consistent and reproducible environment.

The Docker setup ensures that the application behaves the same way locally, in CI, and in deployment scenarios.

---

## Dockerfile

The Dockerfile is responsible for:

- Setting up the Python environment
- Installing project dependencies
- Copying application source code
- Including templates and static files
- Initialising the database
- Seeding initial data
- Running the application using Gunicorn

This ensures the full application is packaged into a single container.

---

## Building the Image

To build the Docker image:

```bash
docker build -f ops/Dockerfile -t devops-quiz .