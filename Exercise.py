from flask import Flask, render_template
import pandas as pd

app = Flask("webpage")


@app.route("/")
def exercise():
    return render_template("exercise.html")


@app.route("/k1/<word>")
def api(word):
    definition = word.upper()
    result_dictionary = {"word": word, "definition":definition}
    return result_dictionary


app.run(debug=True)
