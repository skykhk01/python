__author__ = 'Hwankyu'

'''
    도서관리 ( TKinter 추가하면 DB에 넣기만 하면 됨
              SQLite
              화면에 출력
            )
'''

import tkinter as tk
import tkinter.ttk as ttk
import logging
import sqlite3

class DBHandler(logging.Handler):

    initial_sql = """CREATE TABLE IF NOT EXISTS Book(
                        Name text,
                        Author text,
                        Price text
                   );"""

    insertion_sql = """INSERT INTO Book(
                        Name,
                        Author,
                        Price
                   )
                   VALUES (
                        '%(name)s',
                        '%(author)s',
                       '%(price)s'
                   );"""

    show_sql = "SELECT * FROM Book;"

    def __init__(self, db="data.db"):
        logging.Handler.__init__(self)
        self.db = db

        conn = sqlite3.connect(self.db)
        conn.execute(DBHandler.initial_sql)
        conn.commit()

    def emit(self, record):
        sql = DBHandler.insertion_sql % record
        conn = sqlite3.connect(self.db)
        conn.execute(sql)
        conn.commit()

class Example(tk.Frame):

    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.parent = parent

        self.bookNameEntry = tk.StringVar()
        self.bookAuthorEntry = tk.StringVar()
        self.bookPriceEntry = tk.StringVar()

        self.DBHandler = DBHandler()

        self.lb = tk.Listbox()

        self.initUI()

    def initUI(self):

        self.parent.title("Book Manager")
        self.style = ttk.Style()
        self.style.theme_use("default")
        self.pack(fill=tk.BOTH, expand=1)

        self.columnconfigure(0, pad=3)
        self.columnconfigure(1, pad=3)
        self.columnconfigure(2, pad=3)
        self.columnconfigure(3, pad=3)

        self.rowconfigure(0, pad=3)
        self.rowconfigure(1, pad=3)
        self.rowconfigure(2, pad=3)
        self.rowconfigure(3, pad=3)
        self.rowconfigure(4, pad=3)
        self.rowconfigure(5, pad=3)

        tk.Label(self, text="name : ").grid(row=0, column=0)
        tk.Entry(self, textvariable=self.bookNameEntry).grid(row=0, column=1)

        tk.Label(self, text="author : ", anchor="e").grid(row=1, column=0)
        tk.Entry(self, textvariable=self.bookAuthorEntry).grid(row=1, column=1)

        tk.Label(self, text="price : ", anchor="e").grid(row=2, column=0)
        tk.Entry(self, textvariable=self.bookPriceEntry).grid(row=2, column=1)

        bAdd = ttk.Button(self, text="ADD BOOK", command = lambda : self.clicked_add())
        bAdd.grid(row=3, column=0)

        bDel = ttk.Button(self, text="DELETE BOOK", command = lambda : self.clicked_del())
        bDel.grid(row=4, column=0)

        # bShow = ttk.Button(self, text="SHOW BOOK", command = lambda : self.clicked_show())
        # bShow.grid(row=5, column=0)

        self.lb = tk.Listbox(self)
        self. lb.grid(row=0, column=2, rowspan=5)

        self.clicked_show()

    def clicked_add(self):
        record = dict(name = self.bookNameEntry.get(), author = self.bookAuthorEntry.get(), price = self.bookPriceEntry.get())
        self.DBHandler.emit(record)
        self.lb.insert(tk.END, "{0}, {1}, {2}".format(record["name"], record["author"], record["price"]))

    def clicked_show(self):
        conn = sqlite3.connect("data.db")
        # conn.execute(DBHandler.show_sql)
        # conn.commit()
        cur = conn.cursor()
        cur.execute(DBHandler.show_sql)
        bookList = cur.fetchall()

        for i in bookList:
            content = "{0}, {1}, {2}".format(i[0], i[1], i[2])
            self.lb.insert(tk.END, content)

def main():

    root = tk.Tk()
    ex = Example(root)
    root.geometry("400x250+300+300")
    root.mainloop()


if __name__ == '__main__':
    main()