# UI Tests

## Overview

The UI testing process focuses on validating navigation, layout consistency, and user interaction across the application.

The goal is to ensure that the interface supports the full user journey clearly and reliably.

---

## Navigation Tests

- Check that the home page loads correctly
- Check that navigation follows the correct flow:
  - Home → Login/Register → Rules → Quiz → Result → Ranking → Account
- Check that restricted pages require authentication
- Check that users are redirected appropriately when needed

---

## Form Validation Tests

- Check that all required fields must be completed during registration
- Check that invalid input is rejected
- Check that login validation works correctly
- Check that clear error messages are displayed

---

## Quiz Interface Tests

- Check that questions and answers are displayed clearly
- Check that four answer options are always visible
- Check that user selection is correctly handled
- Check that the prize amount updates correctly
- Check that layout remains consistent across questions

---

## Result Page Tests

- Check that the result page reflects the correct outcome
- Check that the final prize amount is displayed clearly
- Check that the system differentiates between:
  - win
  - lose
  - stop

---

## Ranking and Account Pages

- Check that the ranking page displays stored results correctly
- Check that the account page shows user-specific history
- Check that data is presented clearly and consistently

---

## Responsiveness and Consistency

- Check that pages render correctly at different screen sizes
- Check that layout remains aligned
- Check that fonts, spacing, and visual elements are consistent

---

## Summary

These UI tests ensure that the application provides a consistent, clear, and functional interface that supports the complete system flow.