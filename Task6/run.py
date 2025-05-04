import csv
import numpy as np
import matplotlib.pyplot as plt
from scipy.ndimage import uniform_filter1d

# Шлях до файлу (Змініть його ... або ні)
filename = "-_-.csv"  

# Масиви для збереження прискрення на вісях абциси, ординати і аплікати за проміжок часу
time, x, y, z = [], [], [], []

# Зчитування файлу й завантаження данних до масивів
with open(filename, mode='r', encoding='utf-8-sig') as file:
    reader = csv.DictReader(file)
    for row in reader:
        time.append(float(row['Time (s)']))
        x.append(float(row['Linear Acceleration x (m/s^2)']))
        y.append(float(row['Linear Acceleration y (m/s^2)']))
        z.append(float(row['Linear Acceleration z (m/s^2)']))

# Обрахунок модулю прискорення
c2Mag = np.sqrt(np.array(x)**2 + np.array(y)**2 + np.array(z)**2)

# Фільтрування данних за ковзним середнім 
c2Filtered= uniform_filter1d(c2Mag , size=10)

# Вивід данних
plt.figure(figsize=(10, 5))
plt.plot(time, c2Mag, label="Raw Magnitude", alpha=0.3)
plt.plot(time, c2Filtered, label="Filtered Magnitude", linewidth=2)
plt.title("Filtered Acceleration Magnitude")
plt.xlabel("Time (s)")
plt.ylabel("Acceleration (m/s²)")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()

# Вивід середнього прискорення під час ходьби, прискореної ходьби й бігу
walk = c2Filtered[(c2Filtered > 0.5) & (c2Filtered <= 1.5)]
fastWalk = c2Filtered[(c2Filtered > 1.5) & (c2Filtered <= 3.0)]
run = c2Filtered[c2Filtered > 3.0]

print("Median acceleration during walk:", np.mean(walk))
print("Median acceleration during fast walk:", np.mean(fastWalk))
print("Median acceleration during run:", np.mean(run))