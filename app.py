from flask import Flask, render_template, request
import numpy as np
import joblib

app = Flask(__name__)

# Load the trained model once
model = joblib.load('saved_model.pkl')

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        try:
            # 1️⃣  Extract and convert form data
            petal_length = float(request.form["petal_length"])
            sepal_length = float(request.form["sepal_length"])
            petal_width  = float(request.form["petal_width"])
            sepal_width  = float(request.form["sepal_width"])

            # 2️⃣  Prepare data and make prediction
            features = np.array(
                [sepal_length, sepal_width, petal_length, petal_width]
            ).reshape(1, -1)

            pred_idx = int(model.predict(features)[0])   # e.g. 0, 1, 2

            # 3️⃣  Map index → species name **without touching the NumPy array**
            species = {0: "Setosa", 1: "Versicolor", 2: "Virginica"}
            result_prediction = species.get(pred_idx, "Unknown")

            # 4️⃣  Render page with result
            return render_template(
                "index.html",
                petal_length=petal_length,
                sepal_length=sepal_length,
                petal_width=petal_width,
                sepal_width=sepal_width,
                result_prediction=result_prediction,
            )

        except Exception as e:
            return render_template("index.html", error=str(e))

    # GET request
    return render_template("index.html")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

