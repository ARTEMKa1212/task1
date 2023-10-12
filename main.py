import numpy as np
import matplotlib.pyplot as plt

x = np.array([-4, -1, 1, 2])
y = np.array([-6, 3, -11, -6])
meaning = np.array([-3, -2, -0.5, 2.5])

def f(x, y, meaning):
    n = len(x)
    m = len(meaning)
    result = np.zeros(m)

    for k in range(m):
        p = np.zeros(n)
        for i in range(n):
            num = 1
            for j in range(n):
                if i != j:
                    num *= (meaning[k] - x[j]) / (x[i] - x[j])
            p[i] = num
        result[k] = np.dot(y, p)

    return result

function = f(x, y, meaning)

for i in range(len(meaning)):
    print("Значение в точке", meaning[i], ":", function[i].round(4))

plt.figure(figsize=(8, 6))
plt.plot(x, y, 'ro', label='Исходные точки')
plt.plot(meaning, function, label='Интерполяция')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid(True)
plt.title('Интерполяция Лагранжа')
plt.show()
