from flask import Flask, render_template


app = Flask(__name__)


# When the user called home it showing home page of Tutorial.html page
@app.route("/")
def home():
    # Render_Templates is searching templates directory Tutorial.html page and
    return render_template("home.html")


@app.route("/api/v1/<station>/<date>")
def about(station, date):
    temperature = 23

    return {"Station": station,
            "Date": date,
            "temperature": temperature}


if __name__ == "__main__":
    # showing error on webpage
    app.run(debug=True)
