import psycopg2


class DateBase:

    def __init__(self, host, user, password):
        self.conn_params = {
            "host": host,
            "user": user,
            "password": password
        }

    def create_db(self, db_name):
        conn = psycopg2.connect(**self.conn_params)
        cur = conn.cursor()
        conn.autocommit = True
        cur.execute(f"DROP DATABASE IF EXISTS {db_name};")
        cur.execute(f"CREATE DATABASE {db_name};")
        self.conn_params["dbname"] = db_name
        print("База данных успешно создана")
        cur.close()
        conn.close()

    def create_table(self, table_name, columns):
        conn = psycopg2.connect(**self.conn_params)
        cur = conn.cursor()
        conn.autocommit = True
        cur.execute(f"DROP TABLE IF EXISTS {table_name}")
        cur.execute(f"""CREATE TABLE {table_name}
(
{" ,".join(columns)}
);""")
        print("Таблица успешно создана")
        cur.close()
        conn.close()

    def add_info(self, table_name, info):
        conn = psycopg2.connect(**self.conn_params)
        cur = conn.cursor()
        conn.autocommit = True
        cur.execute(f"INSERT INTO {table_name} VALUES {" ,".join(info)};")
        print("Информация добавлена")
        cur.close()
        conn.close()
