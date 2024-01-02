import os
from flask import Flask, request, render_template, redirect


# Setting app to be
app = Flask("__name__")


# Set the API KEY of Javascript Maps API
if not os.environ.get("API_KEY") or os.environ.get("API_KEY")=="MY_API_KEY":
    raise RuntimeError("API_KEY not set")


# Homepage of the application
@app.route("/")
def index():
    return render_template("index.html")


# Speed test route handling
@app.route('/testing', methods=["GET", "POST"])
def testing():
    if request.method == "POST":
        timing = request.form.get('timing')
        return render_template("testing.html", timing=timing)
    else:
        return render_template("testing.html", timing=60)


# Flash typing page
@app.route("/flashtyping")
def flashtyping():
    return render_template("flashtyping.html")


# Renders the Contact us page
@app.route("/contactus")
def contactus():
    return render_template("contactus.html", API_KEY=os.environ.get('API_KEY'))
