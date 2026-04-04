# Testing Strategy

Due to changes in team structure, testing responsibilities are shared across the team. In practice, both Tamires and Luan actively contributed to testing, validation, and system verification alongside development work.

The testing approach focuses on validating the application at different levels: application logic, user interface, and containerised execution.

---

## Testing Approach

The project follows a lightweight but practical testing strategy based on:

- Functional validation of core quiz logic
- UI validation through browser interaction
- Container validation using Docker
- Service-level checks using HTTP endpoints

---

## Testing Types

### 1. Functional Testing

Functional testing ensures that the quiz logic behaves as expected.

Examples:
- User can register and log in successfully
- Quiz starts correctly after accepting rules
- Questions are displayed with multiple options
- Correct answers increase the prize amount
- Incorrect answers end the game
- User can choose to stop and keep winnings

---

### 2. UI Testing

UI testing is performed manually using the browser to confirm that:

- Pages load correctly (home, login, register, quiz, result, ranking, account)
- Navigation flows correctly between pages
- Data is displayed properly (user info, prize ladder, history)
- Layout remains readable and consistent

---

### 3. Container Testing (Docker)

The application is tested inside a Docker container to ensure it runs independently of the local environment.

The following validations were performed:

- Docker image successfully builds from the provided Dockerfile
- Container runs and exposes port 5000
- Templates and static files load correctly inside the container
- Database is initialised and seeded automatically during build

This ensures the application is fully containerised and portable.

---

### 4. Service / Health Testing

A health endpoint is used to verify that the application is running correctly inside the container.

Example:
GET /health → returns status "ok"

This is also used in the CI pipeline as a basic availability check.

---

### 5. CI Smoke Testing

GitHub Actions is used to automatically validate the application on push and pull request.

The pipeline performs:
- Docker image build
- Container execution
- Health endpoint verification

This provides quick feedback that the application is deployable.

---

## Shared Testing Responsibilities

Testing is not limited to a single role and is distributed as follows:

- Tamires:
  - Defines expected behaviour
  - Documents testing evidence and scenarios
  - Performs functional and UI validation
  - Verifies system flow and consistency

- Luan:
  - Validates Docker environment and container behaviour
  - Supports CI pipeline execution
  - Assists with system-level testing

- Thomas:
  - Validates core application logic during development

---

## Summary

The testing strategy combines manual validation, container-based testing, and automated CI checks.

Although lightweight, this approach ensures that:
- The application logic works correctly
- The user interface behaves as expected
- The system runs reliably inside a containerised environment

This reflects a practical DevOps-oriented testing approach focused on real system behaviour rather than isolated unit testing.