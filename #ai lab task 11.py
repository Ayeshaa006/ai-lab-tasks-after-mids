#ai lab task 11
import pandas as pd
import numpy as numpy
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn import metrics
import matplotlib.pyplot as pyplot
data = pd.read_csv('amazon.csv')
data = data[data['rating'] != '|']
data['rating'] = pd.to_numeric(data['rating'])
for col in ['discounted_price', 'actual_price', 'discount_percentage', 'rating_count']:
    data[col] = data[col].astype(str).str.replace('₹', '').str.replace(',', '').str.replace('%', '')
    data[col] = pd.to_numeric(data[col], errors='coerce')
data = data.dropna()
Features = ['discounted_price', 'actual_price', 'discount_percentage', 'rating_count']
x = data[Features]
y = pd.factorize(data['rating'].astype(str))[0]
X_train, X_test, Y_train, Y_test = train_test_split(x, y, test_size=0.3, shuffle=True)
model = RandomForestClassifier(n_estimators=100)
model.fit(X_train, Y_train)
Y_pred = model.predict(X_test)
accuracy = metrics.accuracy_score(Y_test, Y_pred)
precision = metrics.precision_score(Y_test, Y_pred, average='weighted', zero_division=0)
f1 = metrics.f1_score(Y_test, Y_pred, average='weighted', zero_division=0)
print(f"Accuracy: {accuracy}")
print(f"precision: {precision}")
print(f"f1 score: {f1}")
pyplot.bar(['accuracy', 'precision', 'f1 score'], [accuracy, precision, f1], color=['#08737f', '#00898a', '#39b48e'])
pyplot.ylim(0, 1)
pyplot.title('Lab 11 result')
pyplot.show()