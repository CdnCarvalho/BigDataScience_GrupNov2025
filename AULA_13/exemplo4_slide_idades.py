import numpy as np

idade = np.array([35, 25, 38, 31, 45, 22, 36, 29, 40, 32])

q1 = np.quantile(idade, 0.25)
q2 = np.quantile(idade, 0.50)
q3 = np.quantile(idade, 0.75)

print('Primeiro quartil (Q1): ', q1)
print('Segundo quartil (Q2): ', q2)
print('Terceiro quartil (Q3): ', q3)