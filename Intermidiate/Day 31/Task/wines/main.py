import pandas as pd
from flask import Flask, render_template

app = Flask(__name__)

wines = pd.read_csv('wines.csv')

# wines = wines[["country"]]

print(wines)

@app.route("/")
def home():
    return render_template("home.html", data = wines.to_html())

if __name__ == "__main__"
