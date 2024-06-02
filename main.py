from src.hh_employer import HH
from src.datebase import DateBase

if __name__ == "__main__":
    a = HH()
    b = a.load_vacancies()
    print(a.vacancies)

    c = DateBase("localhost", "postgres", "200818")
    c.create_db("test")
    c.create_table("test", ["emp_id int PRIMARY KEY", "title varchar(100) NOT NULL", "vacancy text"])



    # "host": "localhost",
    # "dbname": "postgres",
    # "user": "postgres",
    # "password": "200818"