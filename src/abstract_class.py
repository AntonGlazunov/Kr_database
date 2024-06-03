from abc import ABC


class Parser(ABC):
    "Абстрактный клас для получения данных по API"

    def load_vacancies(self):
        pass


class Communication(ABC):
    "Абстрактный класс для взоимодействия с БД"

    def __init__(self):
        self.conn_params = {
            "host": "localhost",
            "dbname": None,
            "user": "postgres",
            "password": "200818"
        }
