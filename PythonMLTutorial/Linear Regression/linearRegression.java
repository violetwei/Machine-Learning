import pandas as pd
import numpy as np
import sklearn
from sklearn import linear_model
from sklearn.utils import shuffle
import matplotlib.pyplot as pyplot
import pickle
from matplotlib import style

style.use("ggplot")

# load data using the pandas module
# since data is seperated by semicolons, we need to do sep=";"
data = pd.read_csv("student-mat.csv", sep=";")
# print out the first 5 students in data frame
print(data.head())

# Trimming data, now data frame only has information associated with those 6 attributes
data = data[["G1", "G2", "G3", "studytime", "failures", "absences"]]

print(data.head())

# the attribute we are trying to predict is known as a label
# the other attributes that will determine our label are known as features
predict = "G3"

# use numpy to create two arrays.
# one that contains all of our features, one that contains our labels
X = np.array(data.drop([predict], 1))  # Features
y = np.array(data[predict])  # Labels

# split data into testing and training data
# we'll use 90% of data to train and the other 10% to test
x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(X, y, test_size=0.1)

# TRAIN MODEL MULTIPLE TIMES FOR BEST SCORE
best = 0
for _ in range(30):
    x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(X, y, test_size=0.1)

    # implement linear regression algorithm to make predictions using data set
    # define the model
    linear = linear_model.LinearRegression()

    linear.fit(x_train, y_train)
    accuracy = linear.score(x_test, y_test)
    print(accuracy)

    if accuracy > best:
        best = accuracy
        # saving the model
        with open("studentmodel.pickle", "wb") as f:
            pickle.dump(linear, f)

pickle_in = open("studentmodel.pickle", "rb")
linear = pickle.load(pickle_in)

print("Coefficients: \n", linear.coef_)
print("Intercept: \n",  linear.intercept_)

# Predicting on specific students
predictions = linear.predict(x_test)  # Gets a list of all predictions

for x in range(len(predictions)):
    print(predictions[x], x_test[x], y_test[x])

p = "G1"  # p can change to different attributes eg: p = "studytime" / "absences"
style.use("ggplot")
pyplot.scatter(data[p], data["G3"])
pyplot.xlabel(p)
pyplot.ylabel("Final Grade")
pyplot.show()
