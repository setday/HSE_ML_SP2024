import click

from loader import import_data, import_model
from model_worker import model_predict
from text_refactorer import refactor_data


@click.command()
@click.option('--data', required=False, help='Data sheet to be trained on or to be predicted.', type=str)
@click.option('--model', required=False, help='Model in pickle format path.', type=str)
@click.option('--vectorizer', required=False, help='Vectorizer in pickle format path.', type=str)
def main(data, model, vectorizer):
    if not data:
        raise ValueError(f'No data to work with!')
    data = import_data(data, allowed_inline=True)
    data = refactor_data(data)

    model_name = model
    vectorizer_name = vectorizer
    mod_vec = import_model(model_name, vectorizer_name)

    predict_data = model_predict(mod_vec, data)
    predict_data = [el[0] for el in predict_data]
    print(*predict_data, sep='\n')


if __name__ == '__main__':
    main()
