import csv
from collections import Counter
def my_mode(sample):
    c = Counter(sample)
    return [k for k, v in c.items() if v == c.most_common(1)[0][1]]
def read_csv(filename):
    result = []
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            result.append(row)
    return result
data = read_csv('titanic.csv')
sale = []
count = []
for i in range(1,len(data)):
    if data[i][5]!='':
        sale.append(data[i][5])
        count.append(i)

print("Мода возраста:",my_mode(sale))
print("Номер пассажиров чей возраст указан:",count)
s=0
sale1 = []
for i in count:
    if (float(data[i][5]) < int(my_mode(sale)[0])+10) and (float(data[i][5]) > int(my_mode(sale)[0])-10):
        sale1.append(data[i][9])

for i in range(len(sale1)):
    sale1[i] = float(sale1[i])
print("Стоимости билетов тех пассажиров, которые попали в диапазон ",sale1)
print("Суммарная стоимость билетов пассажиров , севших в порту Квинстаун,\n в возрастном интервале мода +- 10 позиций:", str(round(sum(sale1),3))+'$')