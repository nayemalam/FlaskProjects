from flask import Flask, render_template

# render_template is a function from flask framework
app = Flask(__name__)

@app.route("/")
def home():
    # render_template() looks for an html file in the templates folder
    return render_template("home.html")

@app.route("/about")
def about():
    return render_template("about.html")

if __name__ == "__main__":
    app.run(debug=True)