from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/formations")
def formations():
    formations_list = [
        "Docker pour les debutants",
        "Introduction a Kubernetes",
        "CI/CD avec GitHub Actions",
        "Supervision avec Prometheus",
    ]
    return render_template("formations.html", formations=formations_list)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000)
