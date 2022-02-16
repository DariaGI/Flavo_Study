import os
from os.path import join
import pandas as pd

with open("species.txt", "r") as inp:
    list_of_spec = inp.read()
    list_of_spec = list_of_spec.split()

# print(list_of_spec)

list_fileread = []

for root, dirs, files in os.walk('C:\\Users\\Artem\\Desktop\\Flav_study\\Flavobacterium-PULs-master\\'):
    for filename in files:
        for lookfor in list_of_spec:
            if filename.startswith(lookfor) and 'sum' in filename:
                list_fileread.append("%s" % join(root, filename))

# print(list_fileread)
#
for m in range(len(list_fileread)):
    # data_for_sp = []
    # data_for_sp.append(list_of_spec[m])
    with open('out.txt', 'a') as out:
        out.write(list_of_spec[m] + ', ')
    with open(list_fileread[m], "r") as txt:
        st_1 = txt.read().replace(';', '-')
        st_2 = st_1.split()
    for el in st_2:
        k = el.split('-')
        for i in k:
            if "GH" in i or "PL" in i or "CBM" in i or "CE" in i or "GT" in i:
                with open('out.txt', 'a') as out:
                    out.write(i + ', ')
                # data_for_sp.append(i)
    with open("out.txt", 'a', encoding="utf8") as out:
        out.write('\n')

# print(data_for_sp)
#
