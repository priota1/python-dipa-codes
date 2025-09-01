# ML loss function 
import numpy as np

# Matrix multiplication
A = np.array([[1, 2], [0, 1]])
B = np.array([[2, 3], [4, 5]])
C = np.array([[2,3], [7,8]])
print("A x B =\n", np.dot(np.dot(A, B,) ,C))

# Error & MSE
y_true = np.array([90, 85, 95])
y_pred = np.array([85, 80, 100])
errors = y_true - y_pred
squared_errors = errors ** 2
mse = np.mean(squared_errors)

print("Errors =", errors)
print("Squared errors =", squared_errors)
print("MSE =", mse)

