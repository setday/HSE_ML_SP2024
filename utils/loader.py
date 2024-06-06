import os

import pandas as pd
import pickle


random_state = 113

def import_data(data, allowed_inline=False):
    if not os.path.exists(data):
        if allowed_inline:
            return { 'text': [data] }
        else:
            raise FileNotFoundError(f'{data} not exists!')
    if data[-4:] != '.csv':
        raise ValueError(f'{data} has unsupported format. Only `csv` is supported!')
    
    out_data = pd.read_csv(data)
    if 'text' not in out_data.columns:
        raise ValueError(f'Wrong data format. No `text` columns / fields.')
    
    out_data['text'] = out_data['text'].astype(str)
    
    return out_data

def import_model(model_name, vectorizer_name):
    if not model_name:
        raise ValueError(f'No model, no result. All done!')
    if os.path.exists(model_name) and os.path.exists(vectorizer_name):
        with open(model_name, 'rb') as file:
            model = pickle.load(file)
        with open(vectorizer_name, 'rb') as file:
            vectorizer = pickle.load(file)
        return (
            model,
            vectorizer
        )
    
    raise FileNotFoundError(f'{model_name} or {vectorizer_name} not exists!')
