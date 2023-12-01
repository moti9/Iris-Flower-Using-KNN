import joblib
from sklearn.datasets import load_iris

def makePrediction(sample):
    iris = load_iris()
    model = joblib.load("iris_model_knn.joblib")
    pred = model.predict(sample)
    # print(pred)
    return iris.target_names[pred[0]]  # Access the first element of the prediction array
