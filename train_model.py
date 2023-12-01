from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler
from sklearn import metrics
import joblib

iris = load_iris()

X = iris.data
y = iris.target

# print(f"Feature names : {iris.feature_names}")
# print(f"Target names : {iris.target_names}")
# print("First 10 rows : \n", X[:10])

#Feature scaling
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X) 


#spilit the data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# print(X_train.shape)
# print(X_test.shape)
# print(y_train.shape)
# print(y_test.shape)

#train the model

classifier_knn = KNeighborsClassifier()
classifier_knn.fit(X_train, y_train)

# Make predictions
y_predict = classifier_knn.predict(X_test)

# Model evaluation
accuracy = metrics.accuracy_score(y_test, y_predict)
classification_report = metrics.classification_report(y_test, y_predict)
confusion_matrix = metrics.confusion_matrix(y_test, y_predict)

print(f"Accuracy: {accuracy}")
print("Classification Report:\n", classification_report)
print("Confusion Matrix:\n", confusion_matrix)

# Save the model
joblib.dump(classifier_knn, "iris_model_knn.joblib")
