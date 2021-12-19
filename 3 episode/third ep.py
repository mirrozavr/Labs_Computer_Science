import matplotlib.pyplot as plt
import collections


def list_of_teachers(fail_name):
    f = open(fail_name, 'r')
    prep = []
    while True:
        line = f.readline()
        if not line:
            break
        for i in range(0, len(line.split(';')) - 1, 3):
            prep.append(line.split(';')[i])
    Prep = list(set(prep))
    Prep.sort()
    f.close()
    return Prep


def list_of_group(fail_name):
    f = open(fail_name, 'r')
    group = []
    while True:
        line = f.readline()
        if not line:
            break
        for i in range(1, len(line.split(';')), 3):
            group.append(line.split(';')[i])
    Group = list(set(group))
    Group.sort()
    f.close()
    return Group


marks = list()
data = collections.defaultdict(list)

marks1 = list()
data1 = collections.defaultdict(list)

for i in list_of_teachers("students.csv"):
    # print(i)
    prep_marks = []
    f = open("students.csv", 'r')
    while True:
        line = f.readline()
        # print(line)
        if not line:
            f.close()
            break
        if line.split(';')[0] == str(i):
            prep_marks.append(line.split(';')[2])
            # print(prep_marks)
    for k in range(3, 11, 1):
        marks.append(str(prep_marks).count(str(k)))
        # print(marks)
    for k in range(3, 11, 1):
        data[i].append(int(str(prep_marks).count(str(k))))
        # print(data)
    f.close()

for i in list_of_group("students.csv"):
    group_marks = []
    f = open("students.csv", 'r')
    while True:
        line = f.readline()
        if not line:
            f.close()
            break
        if line.split(';')[1] == str(i):
            group_marks.append(line.split(';')[2])
    for k in range(3, 11, 1):
        marks1.append(str(group_marks).count(str(k)))
    for k in range(3, 11, 1):
        data1[i].append(int(str(group_marks).count(str(k))))
    f.close()


# Первый график
value3 = []
value4 = []
value5 = []
value6 = []
value7 = []
value8 = []
value9 = []
value10 = []
for k, v in data.items():
    value3.append(v[0])
    value4.append(sum(v[0:2]))
    value5.append(sum(v[0:3]))
    value6.append(sum(v[0:4]))
    value7.append(sum(v[0:5]))
    value8.append(sum(v[0:6]))
    value9.append(sum(v[0:7]))
    value10.append(sum(v[0:8]))

DATA3 = {'prep1': value3[0], 'prep2': value3[1], 'prep3': value3[2], 'prep4': value3[3], 'prep5': value3[4],
         'prep6': value3[5], 'prep7': value3[6]}
DATA4 = {'prep1': value4[0], 'prep2': value4[1], 'prep3': value4[2], 'prep4': value4[3], 'prep5': value4[4],
         'prep6': value4[5], 'prep7': value4[6]}
DATA5 = {'prep1': value5[0], 'prep2': value5[1], 'prep3': value5[2], 'prep4': value5[3], 'prep5': value5[4],
         'prep6': value5[5], 'prep7': value5[6]}
DATA6 = {'prep1': value6[0], 'prep2': value6[1], 'prep3': value6[2], 'prep4': value6[3], 'prep5': value6[4],
         'prep6': value6[5], 'prep7': value6[6]}
DATA7 = {'prep1': value7[0], 'prep2': value7[1], 'prep3': value7[2], 'prep4': value7[3], 'prep5': value7[4],
         'prep6': value7[5], 'prep7': value7[6]}
DATA8 = {'prep1': value8[0], 'prep2': value8[1], 'prep3': value8[2], 'prep4': value8[3], 'prep5': value8[4],
         'prep6': value8[5], 'prep7': value8[6]}
DATA9 = {'prep1': value9[0], 'prep2': value9[1], 'prep3': value9[2], 'prep4': value9[3], 'prep5': value9[4],
         'prep6': value9[5], 'prep7': value9[6]}
DATA10 = {'prep1': value10[0], 'prep2': value10[1], 'prep3': value10[2], 'prep4': value10[3], 'prep5': value10[4],
          'prep6': value10[5], 'prep7': value10[6]}
# Это номера столбиков ("координаты по ОХ")
bar_numbers = range(len(DATA3))
# Это подписи столбиков
labels = list(DATA3.keys())
# Это значения столбиков
values13 = list(DATA3.values())
values14 = list(DATA4.values())
values15 = list(DATA5.values())
values16 = list(DATA6.values())
values17 = list(DATA7.values())
values18 = list(DATA8.values())
values19 = list(DATA9.values())
values110 = list(DATA10.values())

fig, ax = plt.subplots()

# Сама картинка барчарта строится из номеров столбиков и их значений
ax.bar(bar_numbers, values110, width=0.5, color='magenta', label='10')
ax.bar(bar_numbers, values19, width=0.5, color='purple', label='9')
ax.bar(bar_numbers, values18, width=0.5, color='deeppink', label='8')
ax.bar(bar_numbers, values17, width=0.5, color='blueviolet', label='7')
ax.bar(bar_numbers, values16, width=0.5, color='violet', label='6')
ax.bar(bar_numbers, values15, width=0.5, color='indigo', label='5')
ax.bar(bar_numbers, values14, width=0.5, color='plum', label='4')
ax.bar(bar_numbers, values13, width=0.5, color='hotpink', label='3')
# Потом на оси ОХ задаются положения отсечек с подписями
ax.set_xticks(bar_numbers)
# И текст этих подписей
ax.set_xticklabels(labels)
plt.legend(loc='upper right')
fig.savefig('Teachers.png')

# Второй график
value31 = []
value41 = []
value51 = []
value61 = []
value71 = []
value81 = []
value91 = []
value101 = []
for k, v in data1.items():
    value31.append(v[0])
    value41.append(sum(v[0:2]))
    value51.append(sum(v[0:3]))
    value61.append(sum(v[0:4]))
    value71.append(sum(v[0:5]))
    value81.append(sum(v[0:6]))
    value91.append(sum(v[0:7]))
    value101.append(sum(v[0:8]))

DATA3 = {'751': value31[0], '752': value31[1], '753': value31[2], '754': value31[3], '755': value31[4],
         '756': value31[5]}
DATA4 = {'751': value41[0], '752': value41[1], 'prep3': value41[2], 'prep4': value41[3], 'prep5': value41[4],
         '756': value41[5]}
DATA5 = {'751': value51[0], 'prep2': value51[1], 'prep3': value51[2], 'prep4': value51[3], 'prep5': value51[4],
         '756': value51[5]}
DATA6 = {'751': value61[0], 'prep2': value61[1], 'prep3': value61[2], 'prep4': value61[3], 'prep5': value61[4],
         '756': value61[5]}
DATA7 = {'751': value71[0], 'prep2': value71[1], 'prep3': value71[2], 'prep4': value71[3], 'prep5': value71[4],
         '756': value71[5]}
DATA8 = {'751': value81[0], 'prep2': value81[1], 'prep3': value81[2], 'prep4': value81[3], 'prep5': value81[4],
         '756': value81[5]}
DATA9 = {'751': value91[0], 'prep2': value91[1], 'prep3': value91[2], 'prep4': value91[3], 'prep5': value91[4],
         '756': value91[5]}
DATA10 = {'751': value101[0], 'prep2': value101[1], 'prep3': value101[2], 'prep4': value101[3], 'prep5': value101[4],
          '756': value101[5]}
# Это номера столбиков ("координаты по ОХ")
bar_numbers = range(len(DATA3))
# Это подписи столбиков
labels = list(DATA3.keys())
# Это значения столбиков
values13 = list(DATA3.values())
values14 = list(DATA4.values())
values15 = list(DATA5.values())
values16 = list(DATA6.values())
values17 = list(DATA7.values())
values18 = list(DATA8.values())
values19 = list(DATA9.values())
values110 = list(DATA10.values())

fig, ax = plt.subplots()

# Сама картинка барчарта строится из номеров столбиков и их значений
ax.bar(bar_numbers, values110, width=0.5, color='magenta', label='10')
ax.bar(bar_numbers, values19, width=0.5, color='purple', label='9')
ax.bar(bar_numbers, values18, width=0.5, color='deeppink', label='8')
ax.bar(bar_numbers, values17, width=0.5, color='blueviolet', label='7')
ax.bar(bar_numbers, values16, width=0.5, color='violet', label='6')
ax.bar(bar_numbers, values15, width=0.5, color='indigo', label='5')
ax.bar(bar_numbers, values14, width=0.5, color='plum', label='4')
ax.bar(bar_numbers, values13, width=0.5, color='hotpink', label='3')
# Потом на оси ОХ задаются положения отсечек с подписями
ax.set_xticks(bar_numbers)
# И текст этих подписей
ax.set_xticklabels(labels)
plt.legend(loc='upper right')
fig.savefig('Groups.png')