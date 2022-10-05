from random import randint
retry = 1
spisok = []
p = 0
pol = 0
otr = 0
print("суммы 15-ти рандомных положительных и отрицательных чисел")
while len(spisok) !=15:
    a = randint(-100, 100)
    if a == 0:
        a = randint(-100, 100)
    else:
        spisok.append(a)
while p < len(spisok):
    if spisok[p] > 0:
        pol = pol + spisok[p]
        p += 1
    elif spisok[p] < 0:
        otr = otr + spisok[p]
        p += 1
print('Сумма положительных: ', pol)
print('Сумма отрицательных: ', otr)