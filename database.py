import sqlite3


class Database:

    def __init__(self):
        self.conn = sqlite3.connect("todo.db")
        self.c = self.conn.cursor()
        self.c.execute(""" CREATE TABLE IF NOT EXISTS todos (
                        id INTEGER PRIMARY KEY NOT NULL, 
                        title TEXT NOT NULL,
                        date TEXT NOT NULL
                        )""")
        self.conn.commit()

    def get_todos(self):
        with self.conn:
            self.c.execute("SELECT * FROM todos")
            return self.c.fetchall()

    def add_todo(self, todo):
        with self.conn:
            self.c.execute("INSERT INTO todos (title,date) VALUES (?,?)", (todo.title, todo.date))

    def delete_todo(self, id):
        with self.conn:
            self.c.execute("DELETE FROM todos WHERE id=?", (id,))
