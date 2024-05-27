import requests


class HH():
    """Класс для загрузки данных с HH"""

    def __init__(self):
        self.url = "https://api.hh.ru/employers/"
        self.headers = {'User-Agent': 'HH-User-Agent'}
        self.user_emp_id = [1808, 1740]
        self.params = {'employer_id': self.user_emp_id}
        self.vacancies = None

    def load_vacancies(self):
        self.params['employer_id'] = keyword
        response = requests.get(self.url)
        vacancies = response.json()
        self.vacancies.extend(vacancies)
        while self.params.get('page') != 1:
            response = requests.get(self.url, headers=self.headers, params=self.params)
            vacancies = response.json()['items']
            self.vacancies.extend(vacancies)
            self.params['page'] += 1


# a = HH(1, "1808")
# a.load_vacancies()
user = 1808
response = requests.get(f"https://api.hh.ru/employers/{user}")
vacancies = response.json()
print(vacancies)
print(type(vacancies))