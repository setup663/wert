from sqlite3 import *
from tkinter.messagebox import *


with connect('database.db') as db:
    cursor = db.cursor()
    cursor.execute(""" CREATE TABLE IF NOT EXISTS table1 (id INTEGER PRIMARY KEY, name TEXT,  expenses TEXT )""")


def list_tables():
    cursor.execute("""SELECT name FROM sqlite_master WHERE type = "table" """)
    return cursor.fetchall()


def information():
    cursor.execute("SELECT * FROM table1")
    return cursor.fetchall()


def information2():
    cursor.execute("SELECT * FROM table2")
    return cursor.fetchall()

def show_info():
    msg = 'Кнопка "Добавить" работает следующим образом: указать имя, платеж, индекс, после нажатия создает и добавляет в файл\n\n' \
          'Кнопка "Изменить" работает следующим образом: Сначала надо указать индекс, где изменять столбец name, после указать новый name\n\n' \
          'Кнопка "Удалить" работает следущющим образом: Сначала надо указать индекс, где удалить строку, после нажать кнопку'
    showinfo("Информация", msg)

