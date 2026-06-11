import numpy as np
import matplotlib.pyplot as plt

A = np.array([[2,1],
              [1,2]])

x = np.linspace(-3,3,10)
y = np.linspace(-3,3,10)

points = []

for i in x:
    for j in y:
        points.append([i,j])

points = np.array(points)

transformed = (A @ points.T).T

plt.figure(figsize=(6,6))

plt.scatter(points[:,0], points[:,1], label="Original", alpha = 0.6)
plt.scatter(transformed[:,0], transformed[:,1], label="Transformed", alpha = 0.6)

plt.axhline(0)
plt.axvline(0)

plt.grid(True)
plt.legend()
plt.title("Grid Transformation by Matrix A")

plt.show()