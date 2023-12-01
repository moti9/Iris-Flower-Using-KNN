from flask import Flask, render_template,request
from prediction import makePrediction
app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")

@app.route("/result", methods=["POST","GET"])
def result():
    if request.method == "POST":
        sepalLength = request.form["sepalLength"]
        sepalWidth = request.form["sepalWidth"]
        petalLength = request.form["petalLength"]
        petalWidth = request.form["petalWidth"]

        # print(sepalLength, sepalWidth)
        # print(petalLength, petalWidth)

        flower = {
            "sepalLength" : sepalLength,
            "sepalWidth" : sepalWidth,
            "petalLength" : petalLength,
            "petalWidth" : petalWidth,
        }

        # Now you can use these values for prediction or further processing

        # makePrediction 
        result = makePrediction([[float(sepalLength), float(sepalWidth), float(petalLength), float(petalWidth)]])
        
        # For testing purposes, just print the values
        # result = f"Prediction: {sepalLength}, {sepalWidth}, {petalLength}, {petalWidth}"

        return render_template("result.html", result=result, flower = flower)

    return render_template("result.html")


if __name__== "__main__":
    app.run(debug=True)