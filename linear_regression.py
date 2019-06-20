import numpy as np 
class LinearRegression():
    def _init_(self):
        pass

    def fit_transform(self, X, y):
        pass

    def predict(self, X):
        pass

    def squared_error(self, y, y_pred):
        sqr_err = (1/(2*np.size(y,0))) * np.sum(np.square(np.subtract(y,y_pred)))
        return sqr_err
