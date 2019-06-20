import numpy as np 
class LinearRegression():
    def _init_(self):
        pass

    def fit_transform(self, X, y, learning_rate = 0.01, iter = 10000):
        pass

    def predict(self, X):
        pass

    def cost(self, y, y_pred, theta):
        sqr_err = (1/(2*np.size(y,0))) * np.sum(np.square(np.subtract(y, y_pred)))
        return sqr_err

    def _gradient_descent(self, X, y, theta, learning_rate, iter):
        for i in iter:
            theta = theta - learning_rate * np.sum((X @ theta.T - y) * X, axis = 0)
            cost = self.cost(X, y, theta)