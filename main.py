from flask import Flask, render_template
import pandas as pd

# __name__ always return __main__ class
app = Flask(__name__)


# When the user called home it showing home page of Tutorial.html page
@app.route("/")
def home():
    # Render_Templates is searching templates directory Tutorial.html page and
    return render_template("home.html")


@app.route("/api/v1/<station>/<date>")
def about(station, date):
    # zfill(6) add the zero and calculate value in 6 digit if station value
    # is 10 Result is '000010' and str convert number to string value
    file_name = "data_small/TG_STAID" + str(station).zfill(6) + ".txt"
    df = pd.read_csv(file_name, skiprows=20, parse_dates=["    DATE"])

    # Showing the date and temperature
    temperature = df.loc[df['    DATE'] == date]['   TG'].squeeze() / 10

    return {"Station": station,
            "Date": date,
            "temperature": temperature}


if __name__ == "__main__":
    # showing error on webpage
    # if 5000 port is occupying other service you can change the
    # port of flask but default port is 5000

    app.run(debug=True)
