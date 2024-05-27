from src.hh_employer import HH
from src.vacancy import Vacancy


def search_vacancies(message, user_quantity):
    """
    Функция для поиска вакансий по запросу
    """
    json_vacancies = HH(user_quantity)
    json_vacancies.load_vacancies(message)
    return json_vacancies.vacancies


def top_vacancies(number_vacancies):
    """
    Функция для возвращает топ N вакансий
    """
    if number_vacancies > len(Vacancy.list_object_vacancy):
        print("""Колличество вакансий для сортировки превышает колличество запрошеных вакансий,
предоставлен список всех получееых вакансий отсортированых по убыванию зарплат""")
        Vacancy.sort_vacancy_salary_min()
        return Vacancy.list_object_vacancy[:number_vacancies]
    else:
        Vacancy.sort_vacancy_salary_min()
        return Vacancy.list_object_vacancy[:number_vacancies]