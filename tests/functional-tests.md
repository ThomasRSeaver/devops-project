# Functional Tests

## Overview

The functional testing process focuses on validating the main behaviour of the application from the user perspective.

The goal is to confirm that authentication, gameplay, result handling, ranking, and account history work as expected.

---

## Authentication Tests

- Check that a new user can register successfully
- Check that registration blocks users under 18
- Check that an existing user can log in successfully
- Check that invalid login credentials are rejected
- Check that non-authenticated users are redirected when trying to access protected pages

---

## Rules and Access Control Tests

- Check that the user must view the rules page before starting the quiz
- Check that the user must accept the rules before continuing
- Check that the quiz cannot be accessed without login
- Check that the quiz cannot be accessed without rules acceptance

---

## Quiz Flow Tests

- Check that a quiz question is displayed correctly
- Check that four answer options are shown
- Check that questions appear in random order
- Check that the current prize and prize ladder are displayed
- Check that a correct answer updates progress
- Check that an incorrect answer ends the game
- Check that the user can stop and keep the secured amount

---

## Result Tests

- Check that the result page is displayed after the game ends
- Check that the system supports all three final outcomes:
  - Win
  - Lose
  - Stop
- Check that the final amount is shown correctly
- Check that the number of correct answers is displayed correctly

---

## Persistence and Tracking Tests

- Check that each completed session is stored
- Check that the final amount is recorded correctly
- Check that the session status is recorded correctly
- Check that the ranking page updates with stored results
- Check that the account page displays personal game history

---

## Summary

These functional tests confirm that the core user journey works correctly, from authentication through gameplay to result tracking and stored performance data.