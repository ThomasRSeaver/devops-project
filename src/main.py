from flask import Flask, request, jsonify, render_template, redirect, url_for, session
from src.manageQuiz import questions
from src.auth import create_user, verify_user
from datetime import date, datetime
import random

app = Flask(__name__, template_folder="../templates", static_folder="../static")
app.secret_key = "devops-quiz-secret-key"

START_MONEY = 10


def format_money(amount):
    return f"€{amount:,}"


def get_prize_ladder():
    ladder = []
    amount = START_MONEY
    for _ in range(len(questions)):
        ladder.append(format_money(amount))
        amount *= 2
    return ladder


def start_new_game():
    question_indexes = list(range(len(questions)))
    random.shuffle(question_indexes)

    session["question_order"] = question_indexes
    session["current_index"] = 0
    session["money"] = START_MONEY
    session["game_over"] = False


@app.route("/health")
def health():
    return jsonify(status="ok", service="devops-quiz"), 200


@app.route("/register", methods=["GET", "POST"])
def register():
    error = None
    success = None

    if request.method == "POST":
        full_name = request.form.get("full_name", "").strip()
        email = request.form.get("email", "").strip().lower()
        password = request.form.get("password", "").strip()
        date_of_birth = request.form.get("date_of_birth", "").strip()

        if len(full_name) < 2 or not any(char.isalpha() for char in full_name):
            return render_template("register.html", error="Please enter a valid full name.", success=None)

        if len(password) < 6:
            return render_template("register.html", error="Password must be at least 6 characters long.", success=None)

        try:
            dob = datetime.strptime(date_of_birth, "%Y-%m-%d").date()
            today = date.today()
            age = today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))
            is_18_or_over = age >= 18
        except ValueError:
            return render_template("register.html", error="Invalid date of birth.", success=None)

        if not is_18_or_over:
            return render_template(
                "register.html",
                error="You must be 18 or older to register for this game.",
                success=None
            )

        created, message = create_user(
            full_name=full_name,
            email=email,
            password=password,
            date_of_birth=date_of_birth,
            is_18_or_over=is_18_or_over
        )

        if created:
            success = message
        else:
            error = message

    return render_template("register.html", error=error, success=success)


@app.route("/login", methods=["GET", "POST"])
def login():
    error = None
    success = None

    if request.method == "POST":
        email = request.form.get("email", "").strip().lower()
        password = request.form.get("password", "").strip()

        user = verify_user(email, password)

        if user:
            session["user_id"] = user["id"]
            session["user_name"] = user["full_name"]
            session["user_email"] = user["email"]
            session["is_18_or_over"] = user["is_18_or_over"]
            return redirect(url_for("home"))
        else:
            error = "Invalid email or password."

    return render_template("login.html", error=error, success=success)


@app.route("/logout")
def logout():
    session.pop("user_id", None)
    session.pop("user_name", None)
    session.pop("user_email", None)
    session.pop("is_18_or_over", None)
    session.pop("question_order", None)
    session.pop("current_index", None)
    session.pop("money", None)
    session.pop("game_over", None)
    return redirect(url_for("home"))


@app.route("/")
def home():
    prize_ladder = get_prize_ladder()
    return render_template(
        "index.html",
        top_prize=prize_ladder[-1],
        user_name=session.get("user_name")
    )


@app.route("/start")
def start():
    if "user_id" not in session:
        return redirect(url_for("login"))

    start_new_game()
    return redirect(url_for("quiz"))


@app.route("/quiz", methods=["GET", "POST"])
def quiz():
    if "question_order" not in session or session.get("game_over"):
        return redirect(url_for("start"))

    prize_ladder = get_prize_ladder()
    question_order = session["question_order"]
    current_index = session["current_index"]
    current_money = session["money"]

    if current_index >= len(question_order):
        session["game_over"] = True
        return render_template(
            "result.html",
            score=len(question_order),
            total=len(question_order),
            won_amount=format_money(current_money),
            result_title="Congratulations!",
            result_message="You answered all questions correctly and reached the top prize."
        )

    question = questions[question_order[current_index]]
    options = question.get_options()
    random.shuffle(options)

    if request.method == "POST":
        action = request.form.get("action")

        if action == "stop":
            session["game_over"] = True
            return render_template(
                "result.html",
                score=current_index,
                total=len(question_order),
                won_amount=format_money(current_money),
                result_title="You Chose to Stop",
                result_message="You decided to stop the game and keep your current prize."
            )

        selected = request.form.get("answer")

        if selected == question.answer_text:
            new_money = current_money * 2
            session["money"] = new_money
            session["current_index"] = current_index + 1

            if session["current_index"] >= len(question_order):
                session["game_over"] = True
                return render_template(
                    "result.html",
                    score=len(question_order),
                    total=len(question_order),
                    won_amount=format_money(new_money),
                    result_title="Congratulations!",
                    result_message="You answered all questions correctly and reached the top prize."
                )

            return redirect(url_for("quiz"))

        session["game_over"] = True
        session["money"] = 0
        return render_template(
            "result.html",
            score=current_index,
            total=len(question_order),
            won_amount="€0",
            result_title="Game Over",
            result_message="You answered incorrectly and lost all the money."
        )

    next_amount = current_money * 2
    current_prize_step = current_index

    return render_template(
        "quiz.html",
        question=question,
        options=options,
        index=current_index,
        total=len(question_order),
        current_money=format_money(current_money),
        next_amount=format_money(next_amount),
        prize_ladder=prize_ladder,
        current_prize_step=current_prize_step
    )


if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)