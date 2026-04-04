# Database Design

## Overview

The application uses SQLite to store persistent data related to users, gameplay, ranking, and results.

The database is initialised using a Python script and supports authentication, session tracking, answer recording, and leaderboard generation.

---

## Main Tables

### 1. users

This table stores registered user information.

Fields:
- `id` (Primary Key)
- `full_name`
- `email` (Unique)
- `password_hash`
- `date_of_birth`
- `is_18_or_over`
- `created_at`

Purpose:
- Store user identity and authentication data
- Support login and registration
- Enable account tracking and statistics

---

### 2. questions

This table stores quiz questions and answer options.

Fields:
- `id` (Primary Key)
- `question_text`
- `correct_answer`
- `wrong1`
- `wrong2`
- `wrong3`
- `is_active`

Purpose:
- Store quiz content
- Allow questions to be enabled/disabled
- Support future expansion of question management

---

### 3. prize_levels

This table defines the reward structure of the quiz.

Fields:
- `id` (Primary Key)
- `question_number`
- `prize_amount`

Purpose:
- Represent the prize progression system
- Ensure consistency in reward calculation

---

### 4. game_sessions

This table stores each game played by a user.

Fields:
- `id` (Primary Key)
- `user_id` (Foreign Key → users.id)
- `started_at`
- `ended_at`
- `current_question_index`
- `correct_answers`
- `current_amount`
- `final_amount`
- `status`

Purpose:
- Track each game session
- Store progress and final outcome
- Support ranking and user history

---

### 5. game_answers

This table records answers selected during gameplay.

Fields:
- `id` (Primary Key)
- `session_id` (Foreign Key → game_sessions.id)
- `question_id` (Foreign Key → questions.id)
- `selected_answer`
- `is_correct`
- `answered_at`

Purpose:
- Store user responses
- Track correctness of answers
- Provide detailed gameplay history

---

## Relationships

The database structure follows these relationships:

- One **user** can have multiple **game sessions**
- One **game session** can have multiple **answers**
- Each **answer** is linked to a specific **question**

This is implemented using foreign keys:

- `game_sessions.user_id → users.id`
- `game_answers.session_id → game_sessions.id`
- `game_answers.question_id → questions.id`

---

## Design Considerations

- The database is designed to be simple but structured
- It supports core gameplay features without unnecessary complexity
- Foreign keys ensure relational integrity between users, sessions, and answers
- The structure allows future expansion, such as:
  - More complex scoring systems
  - Difficulty levels
  - Persistent analytics

---

## Summary

The database design provides a clear and structured way to manage users, gameplay, and results.

It supports the functional requirements of the system while aligning with the overall goal of demonstrating DevOps practices through a working, persistent application.