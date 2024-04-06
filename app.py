from flask import Flask, render_template, request

app = Flask(__name__)

# Dictionary of questions and answers
questions_answers = {
    "When is the school fees payments deadline?": "10th - 15th January",
    "When is the deadline for unit registration?": "25th March",
    "When will last semester's results be uploaded in the institution's portal?": "15th - 27th February",
    "What should I do if I have missing marks?": "Visit the examination department in your faculty"
}

# Route for the index page
@app.route("/elite/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        user_name = request.form["user_name"]
        return render_template("more_help.html", user_name=user_name)
    return render_template("index.html")

# Route for handling chat interactions
@app.route("/elite/chat", methods=["POST"])
def chat():
    user_name = request.form["user_name"]
    question = request.form["question"]
    response = questions_answers.get(question, "Sorry, I don't understand that question.")
    return render_template("response.html", user_name=user_name, response=response)

# Route for providing more help
@app.route("/elite/more_help", methods=["POST"])
def more_help():
    user_name = request.form["user_name"]
    return render_template("more_help.html", user_name=user_name)

# Route for accessing live agent options
@app.route("/elite/live_agent", methods=["POST"])
def live_agent():
    user_name = request.form["user_name"]
    return render_template("live_agent.html", user_name=user_name)

if __name__ == "__main__":
    app.run(debug=True)
