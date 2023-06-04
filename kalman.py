import numpy as np
import matplotlib.pyplot as plt

class KalmanFilter:
    def __init__(self, F, B, H, Q, R, x0, P0):
        self.F = F
        self.B = B
        self.H = H
        self.Q = Q
        self.R = R
        self.x = x0
        self.P = P0

    def predict(self, u):
        self.x = np.dot(self.F, self.x) + np.dot(self.B, u)
        self.P = np.dot(self.F, np.dot(self.P, self.F.T)) + self.Q

    def update(self, z):
        y = z - np.dot(self.H, self.x)
        S = np.dot(self.H, np.dot(self.P, self.H.T)) + self.R
        K = np.dot(self.P, np.dot(self.H.T, np.linalg.inv(S)))
        self.x = self.x + np.dot(K, y)
        self.P = np.dot((np.eye(self.P.shape[0]) - np.dot(K, self.H)), self.P)

# define system
F = np.array([[1,0.1],[0,1]])
B = np.array([[0.005],[0.1]])
H = np.array([[1,0]])
Q = np.array([[0.01,0],[0,0.01]])
R = np.array([[0.1]])
x0 = np.array([[0],[0]])
P0 = np.array([[1,0],[0,1]])

# simulate
kf = KalmanFilter(F,B,H,Q,R,x0,P0)

t = np.arange(0, 10, 0.1)
x_true = np.sin(t)
z = x_true + np.random.normal(0, np.sqrt(R[0,0]), size=len(t))
u = 0
x_filtered = []
for i in range(len(t)):
    kf.predict(u)
    kf.update(z[i])
    x_filtered.append(kf.x[0,0])

plt.figure()
plt.plot(t, x_filtered, label='State estimate xhat')
plt.plot(t, z, label='Measurement z')
plt.plot(t, x_true, label='Ideal measurement')
plt.xlabel('Time')
plt.ylabel('Position')
plt.legend()
plt.show()
