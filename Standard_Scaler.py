import numpy as np
import json

class StandardScaler:
    def __init__(self):
        pass

    def mean(self,data):
        mean = data.mean(axis=0)
        return mean
    
    def standard_deviation(self,data):
        std = data.std(axis=0)
        return std
    
    def fit(self,X,Y):
        dictionary = {"meanX":list(self.mean(X)),
                      "standard_deviationX":list(self.standard_deviation(X)),
                      "meanY":self.mean(Y),
                      "standard_deviationY":self.standard_deviation(Y)}
        
        with open('standard_scaler_parameters.json', 'w') as f:
            json.dump(dictionary, f)
           
        standard_scalerX = (X-self.mean(X).T)/self.standard_deviation(X)
        standard_scalerY = (Y-self.mean(Y).T)/self.standard_deviation(Y)
        
        return standard_scalerX,standard_scalerY
    
    def encoder(self,data):
        file = open("standard_scaler_parameters.json")
        parameters = json.load(file)
        
        means = list(parameters.values())[0]
        stds = list(parameters.values())[1]

        encode = (data-np.array(means).T)/np.array(stds)
        return encode
        
    def decoder(self,data):
        file = open("standard_scaler_parameters.json")
        parameters = json.load(file)
        
        means = list(parameters.values())[2]
        stds = list(parameters.values())[3]

        decode = np.multiply(data,np.array(stds))+np.array(means)
        return decode
        
