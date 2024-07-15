import pandas as pd
import pymorphy3
from nltk.corpus import stopwords
import re
from bs4 import BeautifulSoup
from selenium import webdriver
import string


class Parser():

    def dataset_clear(vac):
        emoji_pattern = re.compile("["
                                   u"\U0001F600-\U0001F64F"  # emoticons
                                   u"\U0001F300-\U0001F5FF"  # symbols & pictographs
                                   u"\U0001F680-\U0001F6FF"  # transport & map symbols
                                   u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                                   u"\U00002500-\U00002BEF"  # chinese char
                                   u"\U00002702-\U000027B0"
                                   u"\U00002702-\U000027B0"
                                   u"\U000024C2-\U0001F251"
                                   u"\U0001f926-\U0001f937"
                                   u"\U00010000-\U0010ffff"
                                   u"\u2640-\u2642"
                                   u"\u2600-\u2B55"
                                   u"\u200d"
                                   u"\u23cf"
                                   u"\u23e9"
                                   u"\u231a"
                                   u"\ufe0f"  # dingbats
                                   u"\u3030"
                                   "]+", flags=re.UNICODE)
        ru_stopwords = stopwords.words("russian")
        alf = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
        vac_clear = []
        for row in vac["Vacancy"]:
            punc = string.punctuation + "–—-«»©∙"
            for i in range(len(punc)):
                if punc[i] == "%":
                    row = row.replace("%", " процентов")
                else:
                    row = row.replace(punc[i], " ")

            row = emoji_pattern.sub(r'', row.lower().replace("₽", "руб").replace("\n", " ")).split(" ")

            morph = pymorphy3.MorphAnalyzer()
            # d = {"a": "а", "p": "р", "e": "е", "y": "у", "c": "с", "k": "к", "o": "о", "x": "х", "u": "и"}
            for j in range(len(row)):
                for a in range(len(row[j])):
                    if row[j][a] in string.ascii_lowercase:
                        if bool(set(alf).intersection(set(row[j]))):
                            if row[j][a] == "a":
                                row[j] = row[j][:a] + "а" + row[j][a + 1:]
                            elif row[j][a] == "p":
                                row[j] = row[j][:a] + "р" + row[j][a + 1:]
                            elif row[j][a] == "e":
                                row[j] = row[j][:a] + "е" + row[j][a + 1:]
                            elif row[j][a] == "y":
                                row[j] = row[j][:a] + "у" + row[j][a + 1:]
                            elif row[j][a] == "c":
                                row[j] = row[j][:a] + "с" + row[j][a + 1:]
                            elif row[j][a] == "k":
                                row[j] = row[j][:a] + "к" + row[j][a + 1:]
                            elif row[j][a] == "o":
                                row[j] = row[j][:a] + "о" + row[j][a + 1:]
                            elif row[j][a] == "x":
                                row[j] = row[j][:a] + "х" + row[j][a + 1:]
                            elif row[j][a] == "u":
                                row[j] = row[j][:a] + "и" + row[j][a + 1:]
                            elif row[j][a] == "h":
                                row[j] = row[j][:a] + "н" + row[j][a + 1:]
                            else:
                                row[j] = row[j].replace(row[j][a], " ")
                        else:
                            row[j] = row[j].replace(row[j][a], " ")
                row[j] = row[j].strip()
                if str(morph.parse(row[j])[0].tag.POS) in ["PREP", "CONJ", "PRCL"] or row[j] in ru_stopwords or re.sub(
                        r"\s+", "", row[j], flags=re.UNICODE).isdigit():
                    row[j] = ""
                else:
                    row[j] = morph.normal_forms(row[j])[0]
            while "" in row:
                row.remove("")

            s = ""
            for k in range(len(row)):
                s += row[k]
                if k != len(row) - 1:
                    s += " "
            vac_clear.append(s)

        return vac_clear

    def get_vacancy_text(url):
        text = ""
        driver = webdriver.Edge()
        driver.get(url)

        soup = BeautifulSoup(driver.page_source, 'html.parser')

        if "hh.ru" in url:
            text = soup.find("h1", "bloko-header-section-1").text

            salary = soup.find("div","magritte-text___pbpft_3-0-9 magritte-text_style-primary___AQ7MW_3-0-9 magritte-text_typography-paragraph-2-regular___VO638_3-0-9")
            if str(type(salary)) == "<class 'NoneType'>":
                salary = soup.find("span", "magritte-text___pbpft_3-0-9 magritte-text_style-primary___AQ7MW_3-0-9 magritte-text_typography-label-1-regular___pi3R-_3-0-9")
            text += " " + salary.text

            regex = re.compile('.*description.*')
            results = soup.find_all('p', {'class': regex})
            for temp in results:
                text += " " + temp.text

            regex = re.compile('.*vacancy-section.*')
            vacancy_content = soup.find('div', class_=regex)
            p_tags = vacancy_content.find_all(["p", "ul"])
            for p in p_tags:
                text += " " + str(p)

            regex = re.compile('.*hh_footer$.*')
            results = soup.find('div', {'class': regex})
            if str(type(results)) != "<class 'NoneType'>":
                for temp in results:
                    text += " " + str(temp)

        elif "avito.ru" in url and ("vakansii" in url or "dropshipping" in url):
            text = soup.find("div", "style-titleWrapper-Hmr_5").text

            salary = soup.find("span", "style-price-value-main-TIg6u")
            if str(type(salary)) == "<class 'NoneType'>":
                salary = soup.find("span","magritte-text___pbpft_3-0-9 magritte-text_style-primary___AQ7MW_3-0-9 magritte-text_typography-label-1-regular___pi3R-_3-0-9")
            text += " " + salary.text

            regex = re.compile('.*params-paramsWrapper_oneColumn-uhGJ9.*')
            results = soup.find_all('div', {'class': regex})
            for temp in results:
                text += " " + str(temp)

            regex = re.compile('.*style-item-description-pL_gy.*')
            results = soup.find_all('div', {'class': regex})
            for temp in results:
                text += " " + str(temp)

        elif "superjob.ru" in url:
            text = soup.find("h1", "_3-Il9 _11FhW _1hbre _1LL-n _3Lhi8 _2myqe _3emg_ _1zcvm").text

            regex = re.compile('.*aFXJ6 KC01B.*')
            results = soup.find_all('span', {'class': regex})
            for temp in results:
                text += " " + temp.text

            regex = re.compile('.*-lWKU _2O5D_ _11FhW ayzah _1LL-n.*')
            results = soup.find('div', {'class': regex})
            for temp in results:
                text += " " + temp.text

            regex = re.compile('.*mrLsm _3a7uW _2myqe _3r0vg _3agHj _1zcvm.*')
            results = soup.find('span', {'class': regex})
            for temp in results:
                text += " " + str(temp)

        elif "zarplata.ru" in url:
            text = soup.find("h1", "bloko-header-section-1").text + " " + soup.find("div","magritte-text___pbpft_3-0-9 magritte-text_style-primary___AQ7MW_3-0-9 magritte-text_typography-paragraph-2-regular___VO638_3-0-9").text

            regex = re.compile('.*description.*')
            results = soup.find_all('p', {'class': regex})
            for temp in results:
                text += " " + temp.text

            regex = re.compile('.*g-user-content.*')
            vacancy_content = soup.find('div', class_=regex)
            p_tags = vacancy_content.find_all(["p", "ul"])
            for p in p_tags:
                text += " " + str(p)

            regex = re.compile('.*hh_footer$.*')
            results = soup.find('div', {'class': regex})
            if str(type(results)) != "<class 'NoneType'>":
                for temp in results:
                    text += " " + str(temp)

        driver.quit()

        return text