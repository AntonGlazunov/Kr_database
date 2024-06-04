import pytest

from src.datebase import DateBase


@pytest.fixture
def con_db():
    test_db = DateBase()
    return test_db


def test_create_db(con_db):
    assert con_db.create_db("pytest") == "База данных pytest успешно создана"


def test_create_table(con_db):
    assert con_db.create_table("test_table", ["id_test int PRIMARY KEY",
                                              "text_test text"]) == "Таблица test_table с столбцами id_test int PRIMARY KEY, text_test text успешно создана"
    assert con_db.add_info("test_table",
                           ["(1)", "(2)", "(3)"]) == "Информация (1), (2), (3) в таблицу test_table добавлена"
