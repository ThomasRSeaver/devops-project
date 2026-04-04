# Project Overview

This project is a web-based quiz application inspired by *"Who Wants to Be a Millionaire"*, developed to demonstrate the practical application of DevOps principles through a functional system.

Rather than remaining a simple script-based quiz, the project evolved into a complete interactive application with user authentication, persistent data, structured gameplay, and deployment through a hosted environment.

## System Overview

The application allows users to:

- Create an account and log in securely
- Access the game only after authentication
- Register only if they meet the 18+ age requirement
- Read and accept the game rules before starting
- Play a multi-step quiz game with increasing prize values
- Decide whether to continue or stop and secure their winnings
- Receive a final result based on performance (win, lose, or stop)
- View a personal account page with game history
- View a ranking page with stored game results

The gameplay follows a prize ladder model, starting at €10 and doubling after each correct answer. This creates a clear risk-and-reward structure and makes the user’s decision to continue or stop part of the game experience.

## DevOps Focus

The main purpose of the project is to apply DevOps concepts in a working application, including:

- **Version Control** using GitHub
- **Branch-based workflow** for controlled updates
- **Continuous Integration** using GitHub Actions
- **Containerisation** using Docker
- **Hosted deployment** using Render
- **Testing and validation** through shared team responsibilities

## Current Status

- Full web application implemented
- Registration and login system working
- Age validation included in the registration process
- Rules page included before gameplay
- Quiz flow fully implemented
- Different end states supported: win, lose, and stop
- Ranking and user history stored and displayed
- Docker container builds and runs successfully
- CI pipeline configured and working
- Hosted version available online

## Project Evolution

The project started from an initial Python quiz structure and was gradually expanded into a more complete web application.

Over time, the system was improved with authentication, UI redesign, game session tracking, ranking, account history, Docker support, CI validation, and hosted deployment. This allowed the project to move beyond a simple classroom prototype and become a more realistic DevOps-focused application.

## Final Scope Position

At this final stage, the project focus is no longer on adding major new features, but on ensuring consistency, validation, documentation quality, and submission readiness.

Some possible future improvements were considered during development, but were intentionally left outside the final scope due to time, academic priorities, and the need to keep the system explainable and achievable within the assignment context.

Possible future improvements could include:

- stronger automated test coverage
- more advanced database-driven question management
- expanded game statistics and analytics
- additional UI polish and accessibility improvements
- stronger deployment and monitoring features

These ideas are considered future enhancements rather than part of the final submission scope.