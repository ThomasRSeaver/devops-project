from src.db import get_connection


def get_ranking(limit=10):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT
            gs.id,
            u.full_name,
            gs.correct_answers,
            gs.final_amount,
            gs.status,
            gs.ended_at
        FROM game_sessions gs
        JOIN users u ON gs.user_id = u.id
        WHERE gs.status IN ('won', 'stopped', 'lost')
          AND gs.ended_at IS NOT NULL
        ORDER BY gs.final_amount DESC, gs.correct_answers DESC, gs.ended_at DESC
        LIMIT ?
    """, (limit,))

    rows = cursor.fetchall()
    conn.close()
    return rows


def get_last_winner():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT
            u.full_name,
            gs.final_amount,
            gs.correct_answers,
            gs.ended_at
        FROM game_sessions gs
        JOIN users u ON gs.user_id = u.id
        WHERE gs.status = 'won'
          AND gs.ended_at IS NOT NULL
        ORDER BY gs.ended_at DESC
        LIMIT 1
    """)

    row = cursor.fetchone()
    conn.close()
    return row