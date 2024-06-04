import psycopg2

from src.abstract_class import Communication


class DateBase(Communication):

    def __init__(self):
        super().__init__()

    def create_db(self, db_name):
        conn = psycopg2.connect(**self.conn_params)
        cur = conn.cursor()
        conn.autocommit = True
        cur.execute(f"DROP DATABASE IF EXISTS {db_name};")
        cur.execute(f"CREATE DATABASE {db_name};")
        self.conn_params["dbname"] = db_name
        print(f"База данных {db_name} успешно создана")
        cur.close()
        conn.close()
        return f"База данных {db_name} успешно создана"

    def create_table(self, table_name, columns: list):
        conn = psycopg2.connect(**self.conn_params)
        cur = conn.cursor()
        conn.autocommit = True
        cur.execute(f"DROP TABLE IF EXISTS {table_name}")
        cur.execute(f"""CREATE TABLE {table_name}
(
{", ".join(columns)}
);""")
        print(f"Таблица {table_name} с столбцами {", ".join(columns)} успешно создана")
        cur.close()
        conn.close()
        return f"Таблица {table_name} с столбцами {", ".join(columns)} успешно создана"

    def add_info(self, table_name, info):
        conn = psycopg2.connect(**self.conn_params)
        cur = conn.cursor()
        conn.autocommit = True
        cur.execute(f"INSERT INTO {table_name} VALUES {", ".join(info)};")
        print(f"Информация в таблицу {table_name} добавлена")
        cur.close()
        conn.close()
        return f"Информация {", ".join(info)} в таблицу {table_name} добавлена"