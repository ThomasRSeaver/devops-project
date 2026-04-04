# UI Tests

## Overview

The UI testing process focuses on validating the visual structure, navigation flow, and user interaction across the application.

The goal is to ensure that the interface supports the user journey clearly and consistently.

---

## Navigation Tests

- Check that the home page loads correctly
- Check that navigation between pages works as expected:
  - Home → Login → Quiz → Result → Ranking → Account
- Check that users cannot access restricted pages without login
- Check that redirects occur correctly when required

---

## Form Validation Tests

- Check that the registration form requires all fields
- Check that invalid inputs are rejected
- Check that login form validation works correctly
- Check that error messages are displayed clearly

---

## Quiz Interface Tests

- Check that questions and answer options are clearly displayed
- Check that answer buttons respond correctly to user input
- Check that the layout remains consistent across questions
- Check that the current prize is displayed clearly

---

## Result Page Tests

- Check that the result page displays the correct outcome
- Check that the final amount is clearly visible
- Check that the user receives appropriate feedback based on:
  - win
  - lose
  - stop

---

## Ranking and Account Pages

- Check that the ranking page displays top players correctly
- Check that the account page shows user-specific data
- Check that layout and alignment remain consistent

---

## Responsiveness and Consistency

- Check that pages render correctly in different browser sizes
- Check that layout elements remain aligned
- Check that fonts, spacing, and colours are consistent across pages

---

## Summary

These UI tests ensure that the application provides a clear, consistent, and functional user interface that supports the overall system flow.