# Requirements

## Team Roles

- Business Analyst: Tamires
- Developer: Thomas
- IT Operations: Luan
- Testing: Shared across the team

---

## Functional Requirements

### User Management

- The system must allow users to register with:
  - Full name
  - Email
  - Password
  - Date of birth
- The system must validate that the user is 18 years or older
- The system must allow registered users to log in
- The system must restrict access to the game for non-authenticated users

---

### Game Access and Rules

- The system must display a rules page before the game starts
- The user must explicitly accept the rules before playing
- The system must prevent access to the quiz if rules are not accepted

---

### Quiz Gameplay

- The system must present quiz questions one at a time
- Each question must have four possible answers, with one correct answer
- Questions must be presented in random order
- The user must start with €10
- Each correct answer must double the current prize amount
- The system must display the current prize and next prize level

---

### Game Flow Control

- After each question, the user must be able to:
  - Continue to the next question
  - Stop and keep the current prize
- If the user answers incorrectly, the game must end immediately
- The system must support three possible outcomes:
  - Win (all questions answered correctly)
  - Lose (incorrect answer)
  - Stop (user chooses to end the game)

---

### Results and Persistence

- The system must store each game session
- The system must store:
  - Number of correct answers
  - Final prize amount
  - Game status (win, lose, stop)
  - Timestamp of the session
- The system must display a result page after the game ends

---

### Ranking and User Account

- The system must display a ranking page with top players
- The ranking must be ordered by performance
- The system must provide a user account page
- The user account page must show:
  - User details
  - Game history

---

## Non-Functional Requirements

### DevOps and Deployment

- The application must be containerised using Docker
- The container must include:
  - Application code
  - Templates and static files
  - Database initialisation and seed data
- The application must run consistently in a container environment

---

### Continuous Integration

- The project must use GitHub Actions for CI
- The CI pipeline must:
  - Build the Docker image
  - Run the application container
  - Validate the application using a health endpoint

---

### Availability and Validation

- The system must expose a health endpoint for service validation
- The application must be deployable in a hosted environment (Render)

---

## Notes

This project is inspired by *"Who Wants to Be a Millionaire"* and focuses on applying DevOps practices through a real, working system rather than a simplified prototype.