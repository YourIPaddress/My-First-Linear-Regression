import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('data.csv')

def cost_function(w, b, points):
    total_error = 0
    for i in range(len(points)):
        x = points.iloc[i].StudyTime
        y = points.iloc[i].Score
        total_error += ((w*x + b) - y)**2
    total_error = total_error / float(len(points))

def gradient_descent(w_now, b_now, points, L):
    w_gradient = 0
    b_gradient = 0
    m = len(points)
    for i in range(len(points)):
        x = points.iloc[i].StudyTime
        y = points.iloc[i].Score

        w_gradient += (2/m)*((w_now*x + b_now) - y)*x
        b_gradient += (2/m)*((w_now*x + b_now) - y)

    w = w_now - w_gradient * L
    b = b_now - b_gradient * L
    return w,b
    
w = 0
b = 0
L = 0.0001
epochs = 1000
for i in range(epochs):
    w, b = gradient_descent(w, b, data, L)

print(w, b)
plt.scatter(data.StudyTime, data.Score, color="black")
plt.plot(list(range(0, 11)), [w*x + b for x in range(0, 11)], color='red')
plt.show()