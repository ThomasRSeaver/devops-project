# DevOps Project – Python Quiz

This project is a Python-based quiz application inspired by "Who Wants to Be a Millionaire", developed as part of a DevOps team project.

The goal of the project is not only to build an application, but to demonstrate DevOps practices including containerisation, continuous integration, and deployment.

---

## Application Overview

The system allows users to:

- Register and log in securely
- Confirm age eligibility before playing
- Read and accept game rules
- Play a quiz with multiple-choice questions
- Progress through increasing prize levels
- Stop the game and keep winnings
- View final results (win / lose / stop)
- Access a ranking leaderboard
- View personal game history

---

## DevOps Implementation

The project integrates several DevOps practices:

### Containerisation (Docker)
- Full application packaged into a Docker container
- Includes backend, templates, static files, and database setup
- Database is automatically initialised and seeded during build
- Runs consistently across environments

### Continuous Integration (GitHub Actions)
- Docker image is built automatically on push and pull request
- Container is executed in CI environment
- Health endpoint is tested to verify application availability

### Deployment
- Application deployed using Render
- Publicly accessible environment for demonstration and testing

---

## Technologies

- Python (Flask)
- Docker
- GitHub Actions
- SQLite
- HTML / CSS / JavaScript

---

## Project Structure

- `src/` → application logic and database setup  
- `ops/` → Docker configuration  
- `docs/` → project documentation  
- `tests/` → testing strategy and validation  
- `ui/` → local presentation/demo assets  

---

## Running the Project Locally

Build the Docker image:


```
docker build -f ops/Dockerfile -t devops-quiz .
```

---

## Running the Container

To run the application locally:

```
docker run -p 5000:5000 devops-quiz
```

Access the aplication:

```
http://localhost:5000
```

---

## Health Check

The application exposes a health endpoint:

```
curl http://localhost:5000/health
```

Expected response:

```
{"service":"devops-quiz","status":"ok"}
```

---

## Testing Approach

Testing is shared across the team and includes:

- Functional testing of quiz logic
- UI testing through browser interaction
- Container validation using Docker
- CI-based smoke testing via GitHub Actions

---

## Project Status

The project is complete and ready for submission.

The application is:
- Fully functional
- Containerised
- Integrated with CI
- Deployed to a hosted environment

---

## Future Improvements

Due to time constraints, the following improvements were identified but not implemented:

- Enhanced UI/UX design
- Expanded question database
- Persistent external database (e.g. PostgreSQL)
- Advanced automated testing (unit and integration tests)
- Full CI/CD pipeline with automated deployment

---

## Team Contribution

The project evolved collaboratively:

- Initial application structure was provided as a starting point
- Core functionality, system integration, Docker setup, and DevOps workflow were developed and refined by the team

This reflects a practical, team-based DevOps approach where responsibilities overlap and evolve during development.