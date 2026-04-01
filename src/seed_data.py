from src.db import get_connection

QUESTIONS = [
    {
        "question_text": "What is the capital of Poland?",
        "correct_answer": "Warsaw",
        "wrong1": "Kyiv",
        "wrong2": "Krakow",
        "wrong3": "Bratislava"
    },
    {
        "question_text": "Which Irish boxer was the lightweight women's champion from 2019 to 2024?",
        "correct_answer": "Katie Taylor",
        "wrong1": "Constance Markievicz",
        "wrong2": "Mary McAleese",
        "wrong3": "Catherine Connolly"
    },
    {
        "question_text": "What is the longest river in Ireland?",
        "correct_answer": "Shannon",
        "wrong1": "Liffey",
        "wrong2": "Barrow",
        "wrong3": "Suir"
    },
    {
        "question_text": "Which English king was killed at the Battle of Hastings in 1066?",
        "correct_answer": "Harold",
        "wrong1": "William",
        "wrong2": "George",
        "wrong3": "Henry"
    },
    {
        "question_text": "Which scientist invented the telephone?",
        "correct_answer": "Alexander Graham Bell",
        "wrong1": "Albert Einstein",
        "wrong2": "Marie Curie",
        "wrong3": "Thomas Edison"
    },
    {
        "question_text": "What year did Michael Jackson release Thriller?",
        "correct_answer": "1982",
        "wrong1": "1973",
        "wrong2": "1992",
        "wrong3": "1830"
    },
    {
        "question_text": "Who plays the Doctor in the newest season of Doctor Who?",
        "correct_answer": "Ncuti Gatwa",
        "wrong1": "David Tennant",
        "wrong2": "Matt Smith",
        "wrong3": "Benedict Cumberbatch"
    },
    {
        "question_text": "Which actor plays Iron Man in the Marvel franchise?",
        "correct_answer": "Robert Downey Jr",
        "wrong1": "Josh Brolin",
        "wrong2": "Robert Pattinson",
        "wrong3": "Chris Hemsworth"
    },
    {
        "question_text": "How many bones are in the human body?",
        "correct_answer": "206",
        "wrong1": "195",
        "wrong2": "214",
        "wrong3": "300"
    },
    {
        "question_text": "Which one of these is not a Teenage Mutant Ninja Turtle?",
        "correct_answer": "Masaccio",
        "wrong1": "Donatello",
        "wrong2": "Michelangelo",
        "wrong3": "Raphael"
    }
]

PRIZE_LEVELS = [10, 20, 40, 80, 160, 320, 640, 1280, 2560, 5120]


def seed_questions():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT COUNT(*) as count FROM questions")
    question_count = cursor.fetchone()["count"]

    if question_count == 0:
        for q in QUESTIONS:
            cursor.execute("""
                INSERT INTO questions (
                    question_text,
                    correct_answer,
                    wrong1,
                    wrong2,
                    wrong3,
                    is_active
                ) VALUES (?, ?, ?, ?, ?, 1)
            """, (
                q["question_text"],
                q["correct_answer"],
                q["wrong1"],
                q["wrong2"],
                q["wrong3"]
            ))

    cursor.execute("SELECT COUNT(*) as count FROM prize_levels")
    prize_count = cursor.fetchone()["count"]

    if prize_count == 0:
        for i, amount in enumerate(PRIZE_LEVELS, start=1):
            cursor.execute("""
                INSERT INTO prize_levels (question_number, prize_amount)
                VALUES (?, ?)
            """, (i, amount))

    conn.commit()
    conn.close()
    print("Questions and prize levels seeded successfully.")


if __name__ == "__main__":
    seed_questions()