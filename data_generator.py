__author__ = 'Hwankyu'

import datetime
import time
import random

dt_today = datetime.datetime.now()
minutes_delta = datetime.timedelta(minutes=1)
end_delta = datetime.timedelta(days=10)

file_name = dt_today.strftime("%Y%m%d_DATA")
start_time = datetime.datetime(dt_today.year, dt_today.month, dt_today.day, 0, 0)
end_time = start_time + end_delta

while start_time < end_time:
    file_name = start_time.strftime("%Y%m%d_DATA")
    data_time = start_time.strftime("%Y%m%d%H%M")

    d1 = random.randrange(1,9999)
    d2 = random.randrange(1,9999)
    d3 = random.randrange(1,9999)

    data = "{0}, {1:4d}, {2:4d}, {3:4d}\n".format(data_time,d1,d2,d3)
    with open(file_name,'a') as f:
       f.write(data)
    print(data)
    start_time = start_time + minutes_delta