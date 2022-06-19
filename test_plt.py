from matplotlib import rcParams
import matplotlib.pyplot as plt
import numpy as np

rcParams['font.family'] = 'Times New Roman', 'Arial', 'Tahoma'
rcParams['font.fantasy'] = 'Times New Roman'

a = 1
x = np.arange(-2*np.pi, 2*np.pi, 0.2)
y = np.sin(x) * np.cos(x)
f = np.sin(x) + np.cos(x)
xz = a*(2*np.cos(x) - np.cos(2*x))
yz = a*(2*np.sin(x) - np.sin(2*x))

# Способ 2 с помощью label

plt.plot(x, f, 'b')
plt.scatter(x, y, color='b')
plt.bar(x, y, color='g', alpha=0.25)
plt.plot(xz, yz, 'r')
plt.scatter([-5.,6], [-2., -1], color='r')

plt.grid(True)
plt.xlabel(u'Аргумент')
plt.ylabel(u'Функция')
plt.title(u'Несколько графиков')

lab1 = u'cos + sin'
lab2 = u'cos * sin'
lab2_5 = u'диаграмма'
lab3 = u'Кардиоида'
lab4 = u'две точки'

plt.legend((lab1, lab3, lab2, lab4, lab2_5), frameon=False)


plt.show()
