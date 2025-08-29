from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return render_template("index.html")

@app.route("/calculate", methods=["POST"])
def calculate():
    # Subjects
    subjects = ["physics", "chemistry", "biology", "maths", "english"]
    obtained_marks = []
    total_marks = []

    for sub in subjects:
        obtained = request.form.get(f"{sub}_obtained", type=float)
        total = request.form.get(f"{sub}_total", type=float)

        if obtained is None or total is None:
            continue
        obtained_marks.append(obtained)
        total_marks.append(total)

    if not total_marks or sum(total_marks) == 0:
        return render_template("index.html", error="Please enter valid marks.")

    total_obtained = sum(obtained_marks)
    total_possible = sum(total_marks)
    percentage = round((total_obtained / total_possible) * 100, 2)

    return render_template("index.html",
                           total_obtained=total_obtained,
                           total_possible=total_possible,
                           percentage=percentage)

if __name__ == "__main__":
    app.run()
