import pandas as pd
import joblib


def predict(filename, algo):

    if algo == "lr":
        model = joblib.load("model_cv_lr.pkl")
    else:
        model = joblib.load("model_cv_mnb.pkl")
        
    return logistic_or_mnb(filename, model)


def logistic_or_mnb(filename, model):

    predicted = []

    data = pd.read_csv(filename)

    n_positive = 0
    n_negetive = 0

    pos = []
    neg = []

    most_negetive_index = 0
    most_positive_index = 0

    for i in range(len(data)):

        prop = {"index": i, "text": "some text", "lable": "some lable", "confidence": 0}

        x = [data["text"][i]]

        prop["lable"] = model.predict(x)[0]

        prop["text"] = data["text"][i]
        

        prop["confidence"] = model.predict_proba(x)[0][0] if model.predict_proba(x)[0][0] > model.predict_proba(x)[0][1] else model.predict_proba(x)[0][1]

        if prop["lable"] == "__label__2":

            prop["lable"] = "+"

            n_positive += 1

        else:
            prop["lable"] = "-"

            n_negetive += 1

        if prop["lable"] == "+":
            pos.append(prop)
        else:
            neg.append(prop)

        predicted.append(prop)

    max = 0
    min = 0

    for i in pos:
        if i["confidence"] > max:
            max = i["confidence"]
            most_positive_index = i["index"]

    for i in neg:
        if i["confidence"] > min:
            min = i["confidence"]
            most_negetive_index = i["index"]
    meter = (-1) * int(((n_negetive - n_positive) / len(predicted)) * 100)

    prop = {
        "index": len(predicted),
        "most_positive_index": most_positive_index,
        "most_negetive_index": most_negetive_index,
        "n_positive": n_positive,
        "n_negetive": n_negetive,
        "total_reviews": len(predicted),
        "meter": meter,
    }

    predicted.append(prop)

    return predicted