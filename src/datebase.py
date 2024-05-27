import psycopg2

class DateBase:

    def __init__(self, db_name):
        self.db_name = db_name
        self.conn_params = {
            "host": "localhost",
            "dbname": "postgres",
            "user": "postgres",
            "password": "200818"
        }

    def con_db(self):
        conn = psycopg2.connect(**self.conn_params)
        cur = conn.cursor()
        conn.autocommit = True
        cur.execute(f"DROP DATABASE IF EXISTS {self.db_name}")
        cur.execute(f"CREATE DATABASE {self.db_name}")
        print("База данных успешно создана")
        cur.close()
        conn.close()

a = DateBase("test1")
a.con_db()
