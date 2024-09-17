# 1-ое задание.
import numpy as np
import matplotlib.pyplot as plt

T_zadan = 6
T_baz = 6
Z_s = 18

k = Z_s / T_baz
z_values = np.linspace(0, T_baz, 100)

P_exp = Z_s * (1 - np.exp(-k * z_values))  # P*(1-e**(-kz))
P_linear = k * z_values              #  P=kz

plt.figure(figsize=(10, 6))
plt.plot(z_values, P_exp, label='P*(1-e^(-kz))', color='blue')
plt.plot(z_values, P_linear, label='P=kz', color='red', linestyle='--')
plt.title('Распределение затрат для подсистем ВС')
plt.xlabel('Срок службы (z)')
plt.ylabel('Сумма затрат (P)')
plt.axhline(y=Z_s, color='purple', linestyle=':', label='Предельная сумма затрат (Z_s)')
plt.axvline(x=T_zadan, color='green', linestyle=':', label='Заданный срок службы (T_zadan)')
plt.legend()
plt.grid()
plt.show()
