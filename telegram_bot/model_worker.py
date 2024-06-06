import sys, os.path

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from utils.loader import import_model
from utils.model_worker import model_predict
from utils.text_refactorer import refactor_data

mod_vec = import_model("models/RandomForestClassifier.pkl", "models/TfidfVectorizer.pkl")

def predict_rating(text: str) -> int:
    text = refactor_data([text])
    pred = model_predict(mod_vec, { 'text': text })

    result = []
    for i in range(len(pred)):
        if pred[i] > 0.8:
            result.append("Определенно токсичный")
        elif pred[i] > 0.5:
            result.append("Возможно токсичный")
        else:
            result.append("Нейтральный")

    return result
