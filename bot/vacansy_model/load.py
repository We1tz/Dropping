import joblib
from vacansy_pipline import VacansyPipline
import os

current_dir = os.path.dirname(__file__)
model_path = os.path.join(current_dir, 'vacancy_model.pkl')
model = joblib.load(model_path)

pipeline = VacansyPipline()


def check_text_vacancy(t):
    x = pipeline.preprocess_text(text=t)
    return model.predict(x)


def check_photo_vacancy(photo_path):
    x = pipeline.preprocess_img(photo_path)
    return model.predict(x)


def check_url_vacancy(url):
    x = pipeline.preprocess_html(url)
    return model.predict(x)


