__author__ = 'Hwankyu'

import glob
import pprint

file_list = glob.glob("*_DATA")
# pprint.pprint(file_list)
with open('DATA', 'a') as mf:
    for x in file_list:
        with open(x, 'r') as rf:
            mf.write(rf.read())
