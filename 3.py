import numpy as np
import matplotlib.pyplot as plt
# 3-ое задани
T_zadan = 200
T_baz = 6
Z_s = 2000
scale_factor = 200

num_subsystems = 5
# Распределение затрат на подсистемы
Z_s_subsystems = Z_s / num_subsystems
k = Z_s_subsystems / T_baz
# Обновление значений z_values для учета T_zadan
z_values = np.linspace(0, T_zadan, 100)
# Расчет затрат для заданного срока службы
P_exp = Z_s_subsystems * (1 - np.exp(-k * z_values / scale_factor))  # Формула P*(1-e**(-kz/scale_factor))
P_linear = k * z_values / scale_factor  # Формула P=kz/scale_factor
#Визуализация результатов
plt.figure(figsize=(10, 6))
plt.plot(z_values, P_exp, label='P*(1-e^(-kz/scale_factor))', color='blue')
plt.plot(z_values, P_linear, label='P=kz/scale_factor', color='red', linestyle='--')
plt.title('Распределение затрат для подсистем ВС')
plt.xlabel('Срок службы (z)')
plt.ylabel('Сумма затрат (P)')
plt.axhline(y=Z_s_subsystems, color='purple', linestyle=':', label='Предельная сумма затрат на подсистему (Z_s_subsystems)')
plt.axvline(x=T_zadan, color='green', linestyle=':', label='Заданный срок службы (T_zadan)')
plt.legend()
plt.grid()
plt.show()