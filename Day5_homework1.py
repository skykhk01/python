__author__ = 'Hwankyu'

'''
    parser(시간이름을 가진 데이터)를 읽어서
    DB Handler로 적절한 형태로 바꾸고 내뱉어서
    sqlite3에 넣는
'''

import logging
import sqlite3
import datetime
import time
import random
import glob
import ast

def data_generator():
    dt_today = datetime.datetime.now()
    minutes_delta = datetime.timedelta(minutes=1)
    # 아래의 값을 바꿔주면 된다.
    end_delta = datetime.timedelta(days=1)

    file_name = dt_today.strftime("%Y%m%d_DATA")
    start_time = datetime.datetime(dt_today.year, dt_today.month, dt_today.day, 0, 0)
    end_time = start_time + end_delta

    while start_time < end_time:
        file_name = start_time.strftime("%Y%m%d_DATA")
        data_time = start_time.strftime("%Y%m%d%H%M")

        d1 = random.randrange(1,9999)
        d2 = random.randrange(1,9999)
        d3 = random.randrange(1,9999)

        # data = "{'logTime':\'{0}\', 'num1':\'{1:4d}\', 'num2':\'{2:4d}\', 'num3':\'{3:4d}\'}".format(data_time,d1,d2,d3)
        data = dict(logTime = data_time, num1 = d1, num2 = d2, num3 = d3)

        with open(file_name,'a') as f:
            f.write(str(data) + '\n')

        print(data)
        start_time = start_time + minutes_delta

    # Merge
    file_list = glob.glob("*_DATA")

    with open('DATA', 'a') as mf:
        for x in file_list:
            with open(x, 'r') as rf:
                mf.write(rf.read())

class DBHandler(logging.Handler):

    initial_sql = """CREATE TABLE IF NOT EXISTS DATA(
                        LogTime text,
                        num1 int,
                        num2 int,
                        num3 int
                   );"""

    insertion_sql = """INSERT INTO DATA(
                        LogTime,
                        num1,
                        num2,
                        num3
                   )
                   VALUES (
                        '%(logTime)s',
                        '%(num1)d',
                        '%(num2)d',
                        '%(num3)d'
                   );"""

    show_sql = "SELECT * FROM DATA;"

    def __init__(self, db="data.db"):
        logging.Handler.__init__(self)
        self.db = db
        self.conn = sqlite3.connect(self.db)
        self.conn.execute(DBHandler.initial_sql)
        self.conn.commit()

    def emit(self, record):
        record = ast.literal_eval(record)
        sql = DBHandler.insertion_sql % record
        self.conn.execute(sql)
        self.conn.commit()

    def showAll(self):
        cur = self.conn.cursor()
        cur.execute(DBHandler.show_sql)
        dataList = cur.fetchall()

        for i in dataList:
            print("{0}: {1}, {2}, {3}".format(i[0], i[1], i[2], i[3]))


def main():
    data_generator()
    dbh = DBHandler()

    with open("DATA", "r") as f:
        data = f.readlines()
        idx = 0
        for i in data:
            print(idx)
            idx += 1
            dbh.emit(i)

    dbh.showAll()

if __name__ == "__main__":
    main()