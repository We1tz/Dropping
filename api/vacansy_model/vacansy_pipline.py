from parser import Parser
from imageread import Reader
import pandas as pd


class VacansyPipline:
    def __init__(self):
        self.img_reader = Reader()

    def preprocess_text(self, text):
        df = pd.DataFrame({"Vacancy": [text]})
        return Parser.dataset_clear(df)[0]
    
    def preprocess_img(self, img_path):
        text_from_image = self.img_reader.read_from_img(img_path)
        df = pd.DataFrame({"Vacancy": [text_from_image]})
        return Parser.dataset_clear(df)[0]
    
    def preprocess_html(self, url):
        text_from_url = Parser.get_vacancy_text(url)
        df = pd.DataFrame({"Vacancy": [text_from_url]})
        return Parser.dataset_clear(df)[0]