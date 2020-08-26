from flask import render_template, request, redirect
from app import app

@app.route("/")
def index():
    return "Hello from Flask"

@app.route('/template')
def template():
    return render_template('home.html')

@app.route('/seq', methods=["GET", "POST"])
def sequence():

    if request.method == "POST":
        req = request.form

        sequence = req.get("seq")
        print(sequence)

        return redirect(request.url)

    return render_template('seq.html')