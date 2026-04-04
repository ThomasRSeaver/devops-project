# System Flow

## Overview
The application follows a structured user journey from authentication to gameplay and result tracking.

---

## 1. User Registration and Login

- Users must create an account or log in to access the system
- Authentication ensures that each user has individual progress tracking
- User data is stored and used for ranking and statistics

---

## 2. Age Validation

- After login, the user must confirm they are over 18
- This step ensures basic validation before entering the game
- If the user does not meet the requirement, access is restricted

---

## 3. Rules Screen

- The user is presented with the game rules before starting
- Rules explain:
  - Prize progression
  - Game mechanics
  - Risk of losing progress
- This ensures clarity before gameplay begins

---

## 4. Quiz Gameplay

- The quiz starts with an initial amount (€10)
- Each correct answer doubles the current amount
- Questions are randomly selected
- Each question provides 4 possible answers
- Only one answer is correct

- After each question, the user can:
  - Continue playing
  - Stop and keep current winnings

---

## 5. Result Handling

- If the user answers incorrectly:
  - All winnings are lost
- If the user stops:
  - Current winnings are saved

- The system records:
  - Final amount
  - Game outcome

---

## 6. Ranking and Account

- Ranking page displays top players based on winnings
- Account page shows:
  - User statistics
  - Previous results

---

## Summary

This flow ensures a complete user journey from authentication to gameplay and result tracking, while maintaining a clear structure and supporting the DevOps deployment model.