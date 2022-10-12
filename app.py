import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle

flask_app = Flask(__name__, template_folder='C:/Users/aakash/Desktop/test/final deploy/deploying')

@flask_app.route("/")
def Home():
    return render_template("index.html")

@flask_app.route("/model")
def model():
    return render_template("model.html")

@flask_app.route("/predict", methods = ["POST"])
def predict():
    model = pickle.load(open("flask_model01.pkl", "rb"))
    float_features = [x for x in request.form.values()]
    del float_features[-1]
    float_features=[float(x) for x in float_features]
    print(float_features)
    features = [np.array(float_features)]
    prediction = model.predict(features)
    if float_features[4]==0:
        return render_template("model.html", prediction_text = "The chances of getting H1B is lower")
    elif prediction==1:
        return render_template("model.html", prediction_text = "The chances of getting H1B is Higher")
    else:
        return render_template("model.html", prediction_text = "The chances of getting H1B is Lower")

    

if __name__ == "__main__":
    flask_app.run(debug=False, host='0.0.0.0')