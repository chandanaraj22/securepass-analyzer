from flask import Flask, render_template, request

from analyzer.complexity import analyze_complexity
from analyzer.entropy import calculate_entropy
from analyzer.patterns import detect_patterns
from analyzer.policy import check_policy
from analyzer.recommendations import generate_recommendations
from analyzer.breach_check import is_breached

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():

    result = None

    if request.method == "POST":

        password = request.form["password"]

        complexity = analyze_complexity(password)

        entropy = calculate_entropy(password)

        patterns = detect_patterns(password)

        policy = check_policy(password)

        breached = is_breached(password)

        recommendations = generate_recommendations(
            complexity,
            patterns,
            entropy
        )

        score = (
            complexity["score"] * 15
            + min(int(entropy / 2), 25)
            - len(patterns) * 10
        )

        score = max(0, min(score, 100))

        if score >= 80:
            risk = "Low Risk 🟢"
        elif score >= 50:
            risk = "Medium Risk 🟡"
        else:
            risk = "High Risk 🔴"

        result = {
            "score": score,
            "risk": risk,
            "entropy": entropy,
            "complexity": complexity,
            "patterns": patterns,
            "policy": policy,
            "breached": breached,
            "recommendations": recommendations,
        }

    return render_template(
        "index.html",
        result=result
    )


if __name__ == "__main_":
    app.run(debug=True)