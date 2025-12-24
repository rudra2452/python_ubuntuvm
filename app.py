from flask import Flask, request, render_template_string

app = Flask(__name__)

html = """
<h2>Feedback Dashboard</h2>
<form method="POST">
  Name: <input type="text" name="name"><br><br>
  Place: <input type="text" name="place"><br><br>
  Feedback: <textarea name="feedback"></textarea><br><br>
  <input type="submit" value="Submit">
</form>
{% if name %}
  <h3>Thank you, {{name}} from {{place}}!</h3>
  <p>Your feedback: {{feedback}}</p>
{% endif %}
"""

@app.route("/", methods=["GET", "POST"])
def dashboard():
    if request.method == "POST":
        return render_template_string(
            html,
            name=request.form.get("name", ""),
            place=request.form.get("place", ""),
            feedback=request.form.get("feedback", "")
        )
    return render_template_string(html)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
