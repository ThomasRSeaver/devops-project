# Tests

## Overview

This folder contains documentation describing how the application was tested across different levels.

Testing is shared across the team and focuses on validating real system behaviour rather than isolated unit tests.

---

## Test Types Included

### Functional Tests
Covers core system behaviour such as:
- Authentication (register/login)
- Quiz flow and game logic
- Result handling
- Ranking and user history

---

### UI Tests
Covers:
- Navigation between pages
- Form validation
- Interface consistency
- User interaction flow

---

### Testing Strategy
Describes the overall approach, including:
- Manual validation
- Docker-based testing
- CI smoke testing

---

## DevOps Context

Testing is integrated into the DevOps workflow:

- Local validation using Docker
- Automated validation using GitHub Actions
- Health endpoint used for service verification

This ensures the application is consistently runnable and deployable.

---

## Summary

The testing approach combines functional, UI, and container-based validation to ensure the application behaves correctly across environments.