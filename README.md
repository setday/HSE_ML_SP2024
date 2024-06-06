![GitHub](https://img.shields.io/github/license/setday/HSE_ML_SP2024)
![GitHub last commit](https://img.shields.io/github/last-commit/setday/HSE_ML_SP2024)
![GitHub top language](https://img.shields.io/github/languages/top/setday/HSE_ML_SP2024)
![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/setday/HSE_ML_SP2024)

# HSE_ML_SP2024
HSE University second course ML course final project about toxic comments classification

## Ссылка на презентацию:
[Презентация](https://docs.google.com/presentation/d/13glzvB9G97l3Urqa2Q2wshJdEIHZV06h0y6Kx4dYEKw/edit?usp=sharing)

# Задачи проекта:

1. Подобрать модель для классификации токсичных комментариев
2. Запаковать её в утилиту
3. Собрать свой датасет и дообучить на нём модель
4. Сделать бота в телеграме для использование нашей модели

# Проект разделён на несколько разделов:

- `notebooks` - вся исследовательская работа связанная с задачей
- `models` - обученные модели, которые используются в боте / утилитах
- `utils` - утилиты для работы 'запакованной' модели + сама запакованная модель
- `telegram_bot` - бот
- `data` - датасеты, с помощью которых была обучена модель

## Источники данных:

- [Источник 1](https://www.kaggle.com/datasets/fizzbuzz/cleaned-toxic-comments)
- [Источник 2](https://www.kaggle.com/datasets/reihanenamdari/youtube-toxicity-data)

## Использованная метрика:
f1-score
