import os
import datetime
import numpy as np


def bbbus(folder_name):
    file_names = [f for f in os.listdir(folder) if (os.path.isfile(os.path.join(folder, f)) and ".txt" in f)]

    dates = []
    for f in file_names:
        dates.append(datetime.datetime.fromtimestamp(int(f.split(".")[0].split("-")[-1][:-3])))

    names = []
    presence = np.zeros(shape=(100, len(dates)), dtype=np.int32)

    i = 0
    for f in file_names:
        file = open(folder_name + f, 'r')
        lines = file.readlines()
        flag = False
        for l in lines:
            if flag:
                name = l[:-1]
                if name in names:
                    presence[names.index(name), i] += 1
                else:
                    names.append(name)
            elif "par nom :" in l:
                flag = True
        i += 1

    return dates, names, presence


def bbbus_report(bbbus_result):
    dates, names, presence = bbbus_result

    for d in dates:
        print(d, end=',')
    print()
    for i in range(len(names)):
        print(names[i], end=' ')
        print(presence[i])
    return


if __name__ == "__main__":
    folder = "./dataset/"
    bbbus_report(bbbus(folder))