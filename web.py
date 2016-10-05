from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def index():
        return render_template("index.html")
def about():
        return render_template("about.html")

# debug=True makes it so changes will automatically load
app.run(debug=True)