from flask import Flask, request, jsonify, render_template
from src.manageQuiz import questions

app = Flask(__name__, template_folder="../templates", static_folder="../static")

prize_ladder = [
    "€100",
    "€200",
    "€500",
    "€1,000",
    "€2,000",
    "€4,000",
    "€8,000",
    "€16,000",
    "€32,000",
    "€64,000"
]


@app.route("/health")
def health():
    return jsonify(status="ok", service="devops-quiz"), 200


@app.route("/")
def home():
    return render_template("index.html", top_prize=prize_ladder[-1])


@app.route("/quiz/<int:index>", methods=["GET", "POST"])
def quiz(index):
    score = int(request.args.get("score", 0))

    if index >= len(questions):
        won_amount = prize_ladder[score - 1] if score > 0 else "€0"
        return render_template(
            "result.html",
            score=score,
            total=len(questions),
            won_amount=won_amount
        )

    question = questions[index]

    if request.method == "POST":
        selected = request.form.get("answer")
        if selected == question.answer_text:
            score += 1
        next_index = index + 1
        return f"""
        <html>
            <head>
                <meta http-equiv="refresh" content="0; url=/quiz/{next_index}?score={score}">
            </head>
            <body></body>
        </html>
        """

    options = question.get_options()
    current_prize = prize_ladder[index]

    return render_template(
        "quiz.html",
        question=question,
        options=options,
        index=index,
        total=len(questions),
        score=score,
        current_prize=current_prize,
        prize_ladder=prize_ladder
    )


if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)