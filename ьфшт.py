# 5 Лабораторная работа.
# 1-ое задание.
import numpy as np
import matplotlib.pyplot as plt
# Заданные параметры
T_zadan = 6  # Заданный срок службы
T_baz = 10   # Базовый срок службы
Z_s = 18     # Предельная сумма затрат
# Определяем значение k
k = Z_s / T_baz
# Создаем массив значений z от 0 до T_baz
z_values = np.linspace(0, T_baz, 100)
# Рассчитываем P по обеим формамулaм
P_exp = Z_s * (1 - np.exp(-k * z_values))  # Формула P*(1-e**(-kz))
P_linear = k * z_values              # Формула P=kz
# Визуализация результатов
plt.figure(figsize=(10, 6))
plt.plot(z_values, P_exp, label='P*(1-e^(-kz))', color='blue')
plt.plot(z_values, P_linear, label='P=kz', color='red', linestyle='--')
plt.title('Распределение затрат для подсистем ВС')
plt.xlabel('Срок службы (z)')
plt.ylabel('Сумма затрат (P)')
plt.axhline(y=Z_s, color='grey', linestyle=':', label='Предельная сумма затрат (Z_s)')
plt.axvline(x=T_zadan, color='green', linestyle=':', label='Заданный срок службы (T_zadan)')
plt.legend()
plt.grid()
plt.show()

# 2 Задание
# Заданные параметры
T_zadan = 120  # Заданный срок службы
T_baz = 3  # Базовый срок службы
Z_s = 30  # Предельная сумма затрат
scale_factor = 200  # Коэффициент масштабирования графика
k = Z_s / T_baz

# Обновление значений z_values для учета T_zadan
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
plt.axhline(y=Z_s, color='grey', linestyle=':', label='Предельная сумма затрат (Z_s)')
plt.axvline(x=T_zadan, color='green', linestyle=':', label='Заданный срок службы (T_zadan)')
plt.legend()
plt.grid()
plt.show()

# 3-ое задание.# Заданные параметры
T_zadan = 100  # Заданный срок службы
T_baz = 3  # Базовый срок службы
Z_s = 20000  # Предельная сумма затрат
scale_factor = 200  # Коэффициент масштабирования графика
# Количество подсистем
num_subsystems = 5  # Примерное количество подсистем
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
plt.axhline(y=Z_s_subsystems, color='grey', linestyle=':', label='Предельная сумма затрат на подсистему (Z_s_subsystems)')
plt.axvline(x=T_zadan, color='green', linestyle=':', label='Заданный срок службы (T_zadan)')
plt.legend()
plt.grid()
plt.show()
#Гайдик# Определить количество подсистем: Сколько подсистем мы будем рассматривать.
# Определить доли затрат для каждой подсистемы: Это может быть сделано на основе их относительной важности, потребностей или других факторов.
# Вычислить распределенные затраты: Умножить долю каждой подсистемы на общую сумму затрат \( Z_s \).
# Вывести результаты: Показать, сколько затрат выделяется на каждую подсистему.