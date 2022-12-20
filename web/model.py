import pickle
import os
from app import ROOT

class Model:
    THRESHOLD = 0.46
    def __init__(self, fpath):
        self.model = pickle.load(open(os.path.join(ROOT, fpath), 'rb'))
    
    def preprocess(self, inputs):
        """Encode categorical features """
        columns = ['Age' , 'cholesterol', 'max_heart_rate', 'blood_pressure', 'st_depression', 'chest_pain_type', 'number_of_vessels', 'thal']
        inputs = [inputs[i] for i in columns]
        mapper = {
            'Male': 0, 'Female': 1, 
            # 'Typical Angina': 0, 'Atypical Angina': 1, 'Non-anginal pain': 2, 'Asymptomatic': 3,
            }

        for idx, categorical_feature in enumerate(inputs):
            if categorical_feature in mapper:
                inputs[idx] = mapper[categorical_feature]
        return tuple(map(float, inputs))

    def adjust_predictions(self, y_pred_proba):
        return (y_pred_proba >= Model.THRESHOLD).astype('int')
