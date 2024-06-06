import click

from loader import import_data, import_model
from model_worker import model_predict
from text_refactorer import refactor_data


@click.command()
@click.option('--data', required=True, help='Data sheet to be trained on or to be predicted.', type=str)
@click.option('--model', required=False, help='Model in pickle format path.', type=str, default='models/RandomForestClassifier.pkl')
@click.option('--vectorizer', required=False, help='Vectorizer in pickle format path.', type=str, default='models/TfidfVectorizer.pkl')
def main(data, model, vectorizer):
    if not data:
        raise ValueError(f'No data to work with!')
    data = import_data(data, allowed_inline=True)
    data['text'] = refactor_data(data['text'])

    model_name = model
    vectorizer_name = vectorizer
    mod_vec = import_model(model_name, vectorizer_name)

    predict_data = model_predict(mod_vec, data)
    # predict_data = [el[0] for el in predict_data]
    predict_data_str = []
    for i in range(len(predict_data)):
        if predict_data[i] > 0.8:
            predict_data_str.append('Definitely toxic')
        elif predict_data[i] > 0.5:
            predict_data_str.append('Possibly toxic')
        else:
            predict_data_str.append('Neutral')
    print(*predict_data_str, sep='\n')


if __name__ == '__main__':
    main()
