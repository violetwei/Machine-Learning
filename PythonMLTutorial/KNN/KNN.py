import sklearn
from sklearn.utils import shuffle
from sklearn.neighbors import KNeighborsClassifier
import pandas as pd
import numpy as np
from sklearn import linear_model, preprocessing

# KNN stands for K-Nearest Neighbors. KNN is a machine learning algorithm used for classifying data.
# Rather than coming up with a numerical prediction such as a students grade or stock price
# KNN attempts to classify data into certain categories
# The K-Nearest Neighbor algorithm is good at classification on small data sets that contain few dimensions (features).

# Goal: Using KNN algorithm to classify cars in 4 categories based upon certain features.

# Loading data
data = pd.read_csv("car.data")
print(data.head())  # To check if our data is loaded correctly

# In order to train the K-Nearest Neighbor Classifier we must convert any string data into some kind of a number
# Creating a label encoder object and then use that to encode each column of our data into integers.
le = preprocessing.LabelEncoder()

# method fit_transform() takes a list (each of our columns) and will return to us an array containing our new values.
buying = le.fit_transform(list(data["buying"]))
maint = le.fit_transform(list(data["maint"]))
door = le.fit_transform(list(data["door"]))
persons = le.fit_transform(list(data["persons"]))
lug_boot = le.fit_transform(list(data["lug_boot"]))
safety = le.fit_transform(list(data["safety"]))
cls = le.fit_transform(list(data["class"]))
print(buying)

predict = "class"

# recombine our data into a feature list and a label list
X = list(zip(buying, maint, door, persons, lug_boot, safety))  # features
y = list(cls)

# split our data into training and testing data
x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(X, y, test_size=0.1)

# Creating a KNN Classifier
model = KNeighborsClassifier(n_neighbors=9)

# fit() fit the model using X as training data and y as target values
model.fit(x_train, y_train)

# score() returns the mean accuracy on the given test data and labels
accuracy = model.score(x_test, y_test)
print(accuracy)

# Testing model
predicted = model.predict(x_test)
names = ["unacc", "acc", "good", "vgood"]

for x in range(len(predicted)):
    print("Predicted: ", names[predicted[x]], "Data: ", x_test[x], "Actual: ", names[y_test[x]])
    # KNN model has a unique method that allows for us to see the neighbors of a given data point
    model.kneighbors([x_test[x]], 9, True)
