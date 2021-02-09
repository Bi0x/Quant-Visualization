from flask import Flask, render_template

from chartinit import *

#! Core settings

app = Flask(
    __name__,
    template_folder="templates",
    static_folder="static",
    static_url_path="/static"
)


#! Fore ends

@app.route("/")
def index():
    return render_template("index.html")


#! Data Provider

@app.route("/leftUpperChart")
def left_upper_chart():
    c = totalIncomeChart()
    return c.dump_options_with_quotes()

@app.route("/leftBottomChart")
def left_bottom_chart():
    c = tomorrowHoldingPredictChart()
    return c.dump_options_with_quotes()

@app.route("/midBottomChart")
def mid_upper_chart():
    c = tomorrowTrendPredictChart()
    return c.dump_options_with_quotes()

@app.route("/rightUpperChart")
def right_upper_chart():
    c = tomorrowSelectedPredictChart()
    return c.dump_options_with_quotes()

@app.route("/rightBottomChart")
def right_bottom_chart():
    c = accuracyChart()
    return c.dump_options_with_quotes()

#! Main codes
if __name__ == "__main__":
    app.run()
