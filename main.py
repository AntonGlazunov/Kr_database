from src.datebase import DateBase
from src.dbmanager import DBManager
from src.hh_employer import HH
from src.utils import emp_info
from src.utils import vacancy_info

if __name__ == "__main__":
    print("Введите название базы данных")
    name_db = input()
    vacancies_from_hh = HH()
    vacancies_from_hh.load_vacancies()
    vacancies = vacancies_from_hh.vacancies
    con_db = DateBase()
    con_db.create_db(name_db)
    con_db.create_table("employer", ["emp_id int PRIMARY KEY", "emp_name varchar(100) NOT NULL",
                                     "emp_url varchar(100)"])
    con_db.create_table("vacancy", ["vacancy_id int PRIMARY KEY", "vacancy_name varchar(100) NOT NULL",
                                    "area varchar(100)", "salary_min int", "salary_max int",
                                    "salary_currency varchar(3)", "published_date date", "vacancy_url varchar(100)",
                                    "requirements text", "description text",
                                    "emp_id int REFERENCES employer(emp_id) NOT NULL"])
    con_db.add_info("employer", emp_info(vacancies))
    con_db.add_info("vacancy", vacancy_info(vacancies))
    db_manager = DBManager(name_db)
    print("Список компаний и колличество вакансий в компании:")
    for row in db_manager.get_companies_and_vacancies_count():
        print(row)
    print("Список вакансий с указанием компаний, зарплаты и ссылки:")
    for row in db_manager.get_all_vacancies():
        print(row)
    print("Средняя минимальная зарплата:")
    for row in db_manager.get_avg_salary_min():
        print(row)
    print("Средняя максимальная зарплата:")
    for row in db_manager.get_avg_salary_max():
        print(row)
    print("Список вакансий у которых зарплата выше средней")
    for row in db_manager.get_vacancies_with_higher_salary():
        print(row)
    print("Ведите ключевое слово для поиска по вакансиям:")
    user_request = input()
    for row in db_manager.get_vacancies_with_keyword(user_request):
        print(row)
