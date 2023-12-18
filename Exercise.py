from flask import Flask, render_template
import pandas as pd


app = Flask("webpage")

df = pd.read_csv("dictionary.csv")


@app.route("/")
def exercise():
    return render_template("exercise.html")


@app.route("/k1/<word>")
def api(word):
    definition = df.loc[df["word"] == word]['definition'].squeeze()
    result_dictionary = {'word': word, 'definition': definition}
    return result_dictionary


app.run(debug=True,port=5001)
