from utils.loader import import_model
from utils.model_worker import model_predict
from utils.text_refactorer import refactor_data

model, vectorizer = import_model("../models/model.pkl", "../models/vectorizer.pkl")

def predict_rating(text: str) -> int:
    text = refactor_data([text])[0]
    return model_predict(model, vectorizer, { 'text': text })
