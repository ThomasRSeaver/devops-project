from src.db import get_connection


def create_game_session(user_id):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO game_sessions (
            user_id,
            current_question_index,
            correct_answers,
            current_amount,
            final_amount,
            status
        ) VALUES (?, 0, 0, 0, 0, 'in_progress')
    """, (user_id,))

    session_id = cursor.lastrowid
    conn.commit()
    conn.close()
    return session_id


def update_game_session_progress(session_id, current_question_index, correct_answers, current_amount):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        UPDATE game_sessions
        SET current_question_index = ?,
            correct_answers = ?,
            current_amount = ?
        WHERE id = ?
    """, (current_question_index, correct_answers, current_amount, session_id))

    conn.commit()
    conn.close()


def finish_game_session(session_id, final_amount, status):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        UPDATE game_sessions
        SET final_amount = ?,
            current_amount = ?,
            status = ?,
            ended_at = CURRENT_TIMESTAMP
        WHERE id = ?
    """, (final_amount, final_amount, status, session_id))

    conn.commit()
    conn.close()