import sqlite3

class Database():
    def __init__(self):
        self.connection = sqlite3.connect('db_name')
        self.cursor = self.connection.cursor()
        self.create.db()

    def create_db(self):
        try:
            query = ("CREATE TABLE IF NOT EXISTS users("
                     "id INTEGER PRIMARY KEY AUTOINCREMENT,"
                     "user_name TEXT,"
                     "user_phone TEXT,"
                     "user_email TEXT," 
                     "telegram_id TEXT);")
            self.cursor.execute(query)
            self.connection.commit()
        except sqlite3.Error as error:
            print("Ошибка при создании",error)

    def __del__(self):
        self.cursor.close()
        self.connection.close()