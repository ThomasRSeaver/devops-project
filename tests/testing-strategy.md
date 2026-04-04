# Testing Strategy

## Overview

Testing responsibilities are shared across the team, reflecting a practical DevOps approach where validation is integrated into development and operations.

The testing strategy focuses on verifying the system at multiple levels: application logic, user interface, container execution, and deployment readiness.

---

## Testing Approach

The project follows a lightweight but effective testing approach based on:

- Functional validation of core application behaviour
- UI validation through real user interaction
- Container validation using Docker
- Service validation using HTTP endpoints
- Automated smoke testing through CI

---

## Testing Types

### 1. Functional Testing

Functional testing ensures that the application behaves correctly from a user perspective.

Examples:
- User can register and log in successfully
- Age validation is enforced during registration
- Rules must be accepted before starting the quiz
- Quiz logic updates correctly based on answers
- Game ends correctly on incorrect answers
- User can stop and keep winnings

---

### 2. UI Testing

UI testing is performed manually using the browser to confirm that:

- Pages load correctly (home, login, register, quiz, result, ranking, account)
- Navigation flows correctly between pages
- User data is displayed properly
- Layout remains clear and consistent

---

### 3. Container Testing (Docker)

The application is tested inside a Docker container to ensure consistent execution.

The following validations are performed:

- Docker image builds successfully
- Container runs and exposes port 5000
- Application loads correctly inside the container
- Templates and static files render properly
- Database is initialised during container setup

---

### 4. Service / Health Testing

A health endpoint is used to confirm that the application is running:

Example:
GET /health → returns status "ok"

This endpoint is also used in the CI pipeline.

---

### 5. CI Smoke Testing

GitHub Actions is used to automatically validate the application.

The pipeline performs:
- Docker image build
- Container execution
- Health endpoint verification

This ensures the application remains deployable after changes.

---

## Summary

The testing strategy combines manual validation, container-based testing, and automated CI checks.

This ensures that:
- The application behaves correctly
- The user interface supports the system flow
- The containerised environment runs reliably

The approach reflects a practical DevOps workflow focused on real system behaviour.