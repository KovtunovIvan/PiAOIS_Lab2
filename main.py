from random import randint
import numpy
import numpy as np
import matplotlib.pyplot as plt
import numpy.random as rand

tv_array = []  # экспоненциальное
for i in range(10):
    tv_array.append((rand.exponential(14, 1)))
i = 0
while (i < 10):
    print("Вывод значения температуры воздуха", tv_array[i])
    i = i + 1

lenght = 100  # beta-распределение
tt_array = []
for i in range(10):
    tt_array.append((rand.beta(1, 1) * lenght) + 0)
i = 0
while (i < 10):
    print("Вывод значения температуры теплоносителя", tt_array[i])
    i = i + 1

l = 80  # дирихле
tg_array = []
for i in range(10): tg_array.append((rand.dirichlet((1, 1)) * l))
i = 0
while (i < 10):
    print("Вывод значения температуры ГВС", tg_array[i])
    i = i + 1

i = 0  # рандом integer
ty_array = numpy.random.random_integers(-20, 50, 10)
while (i < 10):
    print("Вывод значения температуры окружающей среды", ty_array[i])
    i = i + 1

tp_array = []  # Биноминальное распределение
for i in range(10):
    tp_array.append((rand.binomial(1, 0.5)))
i = 0
while (i < 10):
    print("Вывод срабатывания датчика протечки", tp_array[i])
    i = i + 1

from datetime import datetime, date, time

datetime.now()
str(datetime.now())

import time

x = []
for i in range(10):
    time.sleep(2)
    x.append(str(datetime.time(datetime.now())))

y = tv_array
# Построение графика
plt.title("Зависимость температуры воздуха в помещении")  # заголовок
plt.xlabel("x")  # ось абсцисс
plt.ylabel("y")  # ось ординат
plt.grid()  # включение отображение сетки
plt.plot(x, y)  # построение графика
plt.show()

y1 = tt_array
plt.title("Зависимость температуры теплоносителя")
plt.xlabel("x")
plt.ylabel("y1")
plt.grid()
plt.plot(x, y1)
plt.show()

y2 = tg_array
plt.title("Зависимость температуры ГВС")
plt.xlabel("x")
plt.ylabel("y2")
plt.grid()
plt.plot(x, y2)
plt.show()

y3 = ty_array
plt.title("Зависимость температуры воздуха ")
plt.xlabel("x")
plt.ylabel("y3")
plt.grid()
plt.plot(x, y3)
plt.show()

y4 = tp_array
plt.title("срабатывание датчика протечки")
plt.xlabel("x")
plt.ylabel("y4")
plt.grid()
plt.plot(x, y4)
plt.show()
