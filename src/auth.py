from src.db import get_connection
from werkzeug.security import generate_password_hash, check_password_hash


def create_user(full_name, email, password, date_of_birth, is_18_or_over):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT id FROM users WHERE email = ?", (email,))
    existing_user = cursor.fetchone()

    if existing_user:
        conn.close()
        return False, "An account with this email already exists."

    password_hash = generate_password_hash(password)

    cursor.execute("""
        INSERT INTO users (
            full_name,
            email,
            password_hash,
            date_of_birth,
            is_18_or_over
        ) VALUES (?, ?, ?, ?, ?)
    """, (
        full_name,
        email,
        password_hash,
        date_of_birth,
        1 if is_18_or_over else 0
    ))

    conn.commit()
    conn.close()
    return True, "Account created successfully."


def get_user_by_email(email):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM users WHERE email = ?", (email,))
    user = cursor.fetchone()
    conn.close()
    return user


def verify_user(email, password):
    user = get_user_by_email(email)

    if not user:
        return None

    if check_password_hash(user["password_hash"], password):
        return user

    return None