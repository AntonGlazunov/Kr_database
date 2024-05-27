import requests

from src.abstract_class import Parser


class HH(Parser):
    """Класс для загрузки данных с HH"""

    def __init__(self):
        self.url = 'https://api.hh.ru/vacancies'
        self.headers = {'User-Agent': 'HH-User-Agent'}
        self.params = {
            'employer_id': [1740, 1808, 10719084, 1111058, 3202190, 9521233, 10774792, 4602050, 2544353, 4934],
            'page': 0, "area": "113"}
        self.vacancies = []

    def load_vacancies(self):
        while self.params.get('page') != 1:
            response = requests.get(self.url, headers=self.headers, params=self.params)
            vacancies = response.json()['items']
            self.vacancies.extend(vacancies)
            self.params['page'] += 1
