
import numpy as np
import pandas as pd

class HeartDiseaseTransformer():
    def __init__(self):
        self._cp_dict = {1: "typical angina",
                         2: "atypical angina",
                         3: "non-anginal pain", 
                         4: "asymptomatic"}
        
        self._restecg_dict = {0: "normal", 
                              1: "wave abnormality", 
                              2: "ventricular hypertrophy"}
        
        self._thal_dict = {3 : "normal",
                           6 : "fixed defect",
                           7 : "reversable defect"}
    
    def preprocess_X(self, data):
        data["cp"].replace(self._cp_dict, inplace = True)
        data["restecg"].replace(self._restecg_dict, inplace = True)
        data["thal"].replace(self._thal_dict, inplace = True)

        return data
    
    def preprocess_y(self, data):
        data = (data > 0).astype(int)
        
        return data
