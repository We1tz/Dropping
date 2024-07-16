import joblib
from vacansy_pipline import VacansyPipline

model = joblib.load('vacancy_model.pkl')


pipline = VacansyPipline()


def check_text_vacancy(text):
    x = pipline.preprocess_text(text=text)
    return model.predict(x)


def check_url_vacancy(url):
    x = pipline.preprocess_html(url)
    return model.predict(x)
#

def check_photo_vacancy(photo_path):
    x = pipline.preprocess_img(photo_path)
    return model.predict(x)

