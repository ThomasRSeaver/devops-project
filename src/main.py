from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <html>
        <head>
            <title>DevOps Quiz App</title>
        </head>
        <body>
            <h1>DevOps Quiz App</h1>
            <p>The application is running successfully.</p>
            <p>Ops check: use <code>/health</code> to verify availability.</p>
        </body>
    </html>
    """

@app.route("/health")
def health():
    return jsonify(status="ok", service="devops-quiz"), 200

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)