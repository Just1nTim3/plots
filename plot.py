import matplotlib.pyplot as plt
import numpy as np
import pandas
from os import listdir

INDEX_400 = 1000
INDEX_800 = 200
DATA_DIR = 'data/'
CSV_EXT = '.CSV'
counter = 1
min = 100000


fig, ax = plt.subplots()
ax.set_xlabel("Długość fali [nm]")
ax.set_ylabel("Absorbancja")
ax.set_xlim(left=300, right=900)


files = listdir("data")

print('Przed normalizacją:')

for file in files:
    csv = pandas.read_csv(DATA_DIR + file, skiprows=1)
    x = csv['WL/nm']
    y = csv['Abs']
    min = min if min < y.loc[INDEX_400] else y.loc[INDEX_400]
    print(file + "\tmax = " + str("{:.4f}".format(y.loc[INDEX_800:INDEX_400].max())) + '\tdlugosc fali: ' + str(x.loc[y.loc[INDEX_800:INDEX_400].idxmax()]))


print('\nPo normalizacji:')

for file in files:
    csv = pandas.read_csv(DATA_DIR + file, skiprows=1)

    x = csv['WL/nm']
    y = csv['Abs']

    if y.loc[INDEX_400] != min:
        multiplier = y.loc[INDEX_400] / min
        y = y.div(multiplier)

    print(file + "\tmax = " + str("{:.4f}".format(y.loc[INDEX_800:INDEX_400].max())) + '\tdlugosc fali: ' + str(x.loc[y.loc[INDEX_800:INDEX_400].idxmax()]))
    ax.plot(x, y, label=file.replace(CSV_EXT, ""))
    counter += 1


ax.set_ylim(bottom=0)
ax.legend()
plt.show()

