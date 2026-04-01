from src.db import get_connection


def save_game_answer(session_id, question_id, selected_answer, is_correct):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO game_answers (
            session_id,
            question_id,
            selected_answer,
            is_correct
        ) VALUES (?, ?, ?, ?)
    """, (
        session_id,
        question_id,
        selected_answer,
        1 if is_correct else 0
    ))

    conn.commit()
    conn.close()