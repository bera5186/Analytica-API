from flask import Flask, request, jsonify
import json
from api_helper import predict
from flask_swagger_ui import get_swaggerui_blueprint

from flask_cors import CORS, cross_origin
# import pandas as pd


app = Flask(__name__)
CORS(app)

SWAGGER_URL = '/docs'
API_URL = '/static/swagger.json'
SWAGGER_BLUEPRINT = get_swaggerui_blueprint(
    SWAGGER_URL, 
    API_URL,
    config={
        'app_name': 'Sentiment Analysis API'
    }
)

app.register_blueprint(SWAGGER_BLUEPRINT, url_prefix=SWAGGER_URL)


@app.route("/predict", methods=["POST", "GET"])
def predict_file():
    if request.method == "POST":
        file = request.files["file"]
        algo = request.form["algo"]

        data = predict(file, algo)
        return jsonify(data)

        

    return "Send some data bitch"


@app.route("/fake")
def fake():
    return jsonify(
        [
            {
                "confidence": 0.9884693026542664,
                "index": 0,
                "lable": "+",
                "text": "i bought the product last week and i have to admit i liked the product. This product has amazing features",
            },
            {
                "confidence": 0.9992623925209045,
                "index": 1,
                "lable": "+",
                "text": "i am amazed with the quality of the product. giving five stars.",
            },
            {
                "confidence": 0.642754077911377,
                "index": 2,
                "lable": "-",
                "text": "it doesnot works for me at all......this product is realy a shit.",
            },
            {
                "confidence": 0.7229446172714233,
                "index": 3,
                "lable": "-",
                "text": "i donot like the product.",
            },
            {
                "confidence": 0.6997010707855225,
                "index": 4,
                "lable": "-",
                "text": "Initially i liked the phone but after some time it started lagging and problem of battery drainage started.",
            },
            {
                "confidence": 0.9998747110366821,
                "index": 5,
                "lable": "+",
                "text": "the product is amazing i just loved it .",
            },
            {
                "index": 6,
                "meter": -65,
                "most_negetive_index": 2,
                "most_positive_index": 5,
                "n_negetive": 3,
                "n_positive": 3,
                "total_reviews": 6,
            },
        ] 
    )


@app.route("/")
def home():
    return "0"


if __name__ == "__main__":
    app.run(debug=True)
