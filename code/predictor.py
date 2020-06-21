
import os
import pickle
import numpy as np
import pandas as pd

class HeartDiseasePredictor(object):
    def __init__(self, model, preprocessor):
        self._model = model
        self._preprocessor = preprocessor

    def predict(self, instances, **kwargs):
        instances = pd.DataFrame(instances, 
             columns = ["age", "sex", "cp", "trestbps", "chol", "fbs", "restecg",
             "thalach", "exang", "oldpeak", "slope","ca", "thal"])
        preprocessed_inputs = self._preprocessor.preprocess_X(instances)
        outputs = self._model.predict_proba(preprocessed_inputs)
        return [str(np.round(p[1],2)*100)+"%" for p in outputs]

    @classmethod
    def from_path(cls, model_dir):
        model_path = os.path.join(model_dir, 'log_model_v1.pkl')
        with open(model_path, 'rb') as f:
            model = pickle.load(f)

        preprocessor_path = os.path.join(model_dir, 'preprocessor.pkl')
        with open(preprocessor_path, 'rb') as f:
            preprocessor = pickle.load(f)
        
        return cls(model, preprocessor)
