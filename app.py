# Original Flask application supplied with the Bachelor project.
# Requires model.pkl, tfidf_vectorizer.pkl, and the templates/ directory.
from flask import Flask, request, render_template
import warnings
import re
import pickle
import pymsgbox

warnings.filterwarnings("ignore")

with open("model.pkl", "rb") as model_file:
    pac = pickle.load(model_file)

with open("tfidf_vectorizer.pkl", "rb") as vectorizer_file:
    tfidf_vectorizer = pickle.load(vectorizer_file)

app = Flask(__name__)

@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html")

@app.route("/performance")
def performance():
    return render_template("performance.html")

@app.route("/chart")
def chart():
    return render_template("chart.html")

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/upload")
def upload():
    return render_template("upload.html")

@app.route("/preview", methods=["POST"])
def preview():
    if request.method == "POST":
        dataset = request.files["datasetfile"]
        import pandas as pd
        df = pd.read_csv(dataset, encoding="unicode_escape")
        df.set_index("Id", inplace=True)
        return render_template("preview.html", df_view=df)

@app.route("/prediction")
def prediction():
    return render_template("prediction.html")

@app.route("/charts", methods=["GET", "POST"])
def charts():
    url_arg = request.args.get("news", "")
    pattern = r"(?:http://)?\\w+\\.\\S*[^.\\s]"
    input_data = re.findall(pattern, url_arg)

    if input_data:
        tfidf_test = tfidf_vectorizer.transform(input_data)
        y_pred = pac.predict(tfidf_test)
        for url in input_data:
            return render_template("prediction.html", preds=str(y_pred[0]), url=url)

    pymsgbox.alert("Enter the url", "warning")
    return render_template("prediction.html")

if __name__ == "__main__":
    app.run(debug=True)
