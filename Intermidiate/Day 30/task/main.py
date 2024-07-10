from flask import Flask, render_template as rt
import pandas as pd
app = Flask(__name__)
df = pd.read_csv("dictionary.csv")


variable = "Hello there"
@app.route("/")
def home():
    return rt("home.html", data=variable)

@app.route("/api/v1/<word>/")
def api(word):
    print("Hi")
    definition = df.loc[df["word"] == word]['definition'].squeeze()
    print(definition)
    result_dictionary = {"word": word,
                         'definition: ': definition}
    return result_dictionary

if __name__ == "__main__":
    app.run(debug=True)