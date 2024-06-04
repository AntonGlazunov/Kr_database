from decimal import Decimal

import pytest

from src.datebase import DateBase
from src.dbmanager import DBManager
from src.hh_employer import HH


@pytest.fixture
def test_dbmanager():
    con_hh = HH()
    con_hh.load_vacancies()
    con_db = DateBase()
    con_db.create_db("pytest")
    con_db.create_table("employer", ["emp_id int PRIMARY KEY", "emp_name varchar(100) NOT NULL",
                                     "emp_url varchar(100)"])
    con_db.create_table("vacancy", ["vacancy_id int PRIMARY KEY", "vacancy_name varchar(100) NOT NULL",
                                    "area varchar(100)", "salary_min int", "salary_max int",
                                    "salary_currency varchar(3)", "published_date date", "vacancy_url varchar(100)",
                                    "requirements text", "description text",
                                    "emp_id int REFERENCES employer(emp_id) NOT NULL"])
    con_db.add_info("employer", ["(1, 'PiP', 'htpps:www.ry')", "(2, 'PaP', 'htpps:ww.ry')"])
    con_db.add_info("vacancy", ["(1, 'a', 'a1', 100, 200, 'RUR', '2024-06-04T13:29:08+0300', 'a3', 'a4', 'a5', 1)",
                                "(2, 'b', 'b1', 0, 200, 'RUR', '2024-06-04T13:29:08+0300', 'b3', 'b4', 'b5', 1)",
                                "(3, 'c', 'c1', 100, 0, 'RUR', '02024-06-04T13:29:08+0300', 'c3', 'c4', 'c5', 2)"])
    con_dbmanager = DBManager("pytest")
    return con_dbmanager


def test_get_companies_and_vacancies_count(test_dbmanager):
    assert test_dbmanager.get_companies_and_vacancies_count() == [('PaP', 1), ('PiP', 2)]


def test_get_all_vacancies(test_dbmanager):
    assert test_dbmanager.get_all_vacancies() == [('a', 'PiP', 100, 200, 'a3'), ('b', 'PiP', 0, 200, 'b3'),
                                                  ('c', 'PaP', 100, 0, 'c3')]


def test_get_avg_salary_min(test_dbmanager):
    assert test_dbmanager.get_avg_salary_min()[0] == (Decimal('100.0000000000000000'),)


def test_get_avg_salary_max(test_dbmanager):
    assert test_dbmanager.get_avg_salary_max()[0] == (Decimal('200.0000000000000000'),)


def test_get_vacancies_with_higher_salary(test_dbmanager):
    assert test_dbmanager.get_vacancies_with_higher_salary() == [('a',), ('b',)]


def test_get_vacancies_with_keyword(test_dbmanager):
    assert test_dbmanager.get_vacancies_with_keyword("a") == [('a',)]
