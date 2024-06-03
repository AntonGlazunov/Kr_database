import psycopg2

from src.abstract_class import Communication


class DBManager(Communication):
    """
    Класс для запросов к БД
    """

    def __init__(self, db_name):
        super().__init__()
        self.conn_params["dbname"] = db_name

    def get_companies_and_vacancies_count(self):
        """Получает список всех компаний и количество вакансий у каждой компании"""
        conn = psycopg2.connect(**self.conn_params)
        cur = conn.cursor()
        conn.autocommit = True
        cur.execute(f"SELECT emp_name, COUNT(vacancy_id) FROM emp "
                    f"JOIN vacancy USING (emp_id) "
                    f"GROUP BY emp_name;")
        all_emp_with_amount_vacancy = cur.fetchall()
        cur.close()
        conn.close()
        return all_emp_with_amount_vacancy

    def get_all_vacancies(self):
        """
        Получает список всех вакансий с указанием названия компании,
        названия вакансии и зарплаты и ссылки на вакансию
        """
        conn = psycopg2.connect(**self.conn_params)
        cur = conn.cursor()
        conn.autocommit = True
        cur.execute(f"SELECT vacancy_name, emp_name, salary_min, salary_max, vacancy_url FROM vacancy "
                    f"JOIN emp USING (emp_id);")
        all_vacancy = cur.fetchall()
        cur.close()
        conn.close()
        return all_vacancy

    def get_avg_salary_min(self):
        """
        Получает среднюю минимальную зарплату по вакансиям
        """
        conn = psycopg2.connect(**self.conn_params)
        cur = conn.cursor()
        conn.autocommit = True
        cur.execute(
            f"SELECT AVG(salary_min) as avg_salary_min FROM vacancy "
            f"WHERE salary_min <> 0;")
        avg_salary_min = cur.fetchall()
        cur.close()
        conn.close()
        return avg_salary_min

    def get_avg_salary_max(self):
        """
        Получает среднюю максимальную зарплату по вакансиям
        """
        conn = psycopg2.connect(**self.conn_params)
        cur = conn.cursor()
        conn.autocommit = True
        cur.execute(
            f"SELECT AVG(salary_max) as avg_salary_max FROM vacancy "
            f"WHERE salary_max <> 0;")
        avg_salary_max = cur.fetchall()
        cur.close()
        conn.close()
        return avg_salary_max

    def get_vacancies_with_higher_salary(self):
        """
        Получает список всех вакансий,
        у которых зарплата выше средней по всем вакансиям
        """
        conn = psycopg2.connect(**self.conn_params)
        cur = conn.cursor()
        conn.autocommit = True
        cur.execute(
            f"SELECT vacancy_name FROM vacancy "
            f"WHERE salary_max <> AVG(salary_max);")
        vacancy_list = cur.fetchall()
        cur.close()
        conn.close()
        return vacancy_list

    def get_vacancies_with_keyword(self, user_request):
        """
        Получает список всех вакансий,
        в названии которых содержатся переданные
        в метод слова, например python
        """
        conn = psycopg2.connect(**self.conn_params)
        cur = conn.cursor()
        conn.autocommit = True
        cur.execute(
            f"SELECT vacancy_name FROM vacancy "
            f"WHERE vacancy_name LIKE '%{user_request}%';")
        user_table = cur.fetchall()
        cur.close()
        conn.close()
        return user_table
