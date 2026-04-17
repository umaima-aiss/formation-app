from flask import Flask, render_template

app = Flask(__name__)

FORMATIONS = [
    "Docker pour les debutants",
    "Introduction a Kubernetes",
    "CI/CD avec GitHub Actions",
    "Supervision avec Prometheus",
]


@app.route("/")
def index():
    return render_template(
        "index.html",
        formations_count=len(FORMATIONS),
        active_page="home",
    )


@app.route("/formations")
def formations():
    return render_template(
        "formations.html",
        formations=FORMATIONS,
        active_page="formations",
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000)
