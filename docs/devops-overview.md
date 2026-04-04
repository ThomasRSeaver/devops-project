# DevOps Overview

## Overview

This project applies core DevOps practices to a simple quiz application, focusing on automation, consistency, and deployment rather than product complexity.

---

## Version Control (GitHub)

- The project is managed using GitHub
- Feature branches are used for development (e.g., `docker-fix`)
- Changes are committed incrementally with descriptive commit messages
- The repository maintains a clear history of development and fixes

---

## Continuous Integration (CI)

- GitHub Actions is used to automate validation
- The CI pipeline runs on push events
- It ensures the application builds and basic checks pass

- This provides:
  - Early detection of issues
  - Consistent validation across environments

---

## Containerisation (Docker)

- The application is fully containerised using Docker
- The container includes:
  - Python environment
  - Application code
  - Dependencies
  - Database setup

- The container ensures:
  - Consistent behaviour across environments
  - Easy local testing and deployment

---

## Health Check

- A `/health` endpoint is implemented
- It returns a JSON response confirming the service is running:

Example:
{"service":"devops-quiz","status":"ok"}

- This endpoint is used to validate:
  - Container status
  - Application availability

---

## Local Validation

The application was tested locally using Docker:

- Container successfully built and started
- Application accessible via browser
- Health check endpoint validated using:

curl http://localhost:5000/health

---

## Deployment (Render)

- The application is deployed using Render
- A hosted environment is available for demonstration:

https://devops-quiz-ylll.onrender.com/

- The deployment includes:
  - Environment variable configuration
  - Automated build and startup process

- The hosted version demonstrates:
  - Real-world deployment capability
  - Public accessibility of the system

---

## Testing Approach

Testing is shared across the team:

- Functional testing of quiz logic
- UI testing via browser interaction
- Smoke testing through Docker and CI

This reflects a practical DevOps approach where testing is integrated into development and operations.

---

## Summary

This project demonstrates the integration of DevOps practices into a simple application, including version control, CI, containerisation, and deployment to a hosted environment.