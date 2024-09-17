import numpy as np
import matplotlib.pyplot as plt
# 2 Задание
# Заданные параметры
T_zadan = 100
T_baz = 6
Z_s = 200
scale_factor = 200
k = Z_s / T_baz

z_values = np.linspace(0, T_zadan, 100)

# Расчет затрат для заданного срока службы
P_exp = Z_s * (1 - np.exp(-k * z_values / scale_factor))  # Формула P*(1-e**(-kz/scale_factor))
P_linear = k * z_values / scale_factor  # Формула P=kz/scale_factor
# Визуализация результатов
plt.figure(figsize=(10, 6))
plt.plot(z_values, P_exp, label='P*(1-e^(-kz/scale_factor))', color='blue')
plt.plot(z_values, P_linear, label='P=kz/scale_factor', color='red', linestyle='--')
plt.title('Распределение затрат для подсистем ВС')
plt.xlabel('Срок службы (z)')
plt.ylabel('Сумма затрат (P)')
plt.axhline(y=Z_s, color='purple', linestyle=':', label='Предельная сумма затрат (Z_s)')
plt.axvline(x=T_zadan, color='green', linestyle=':', label='Заданный срок службы (T_zadan)')
plt.legend()
plt.grid()
plt.show()