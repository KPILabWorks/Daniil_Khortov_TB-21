import numpy as np
from sklearn.preprocessing import MinMaxScaler
from tensorflow.keras.models import Model
from tensorflow.keras.layers import Input, Dense
from scipy.interpolate import interp1d, UnivariateSpline
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt

#Генератор рандому
np.random.seed(42)

#Генератор вибірки зі 100 елементів від 0 до близько 4п. Це до 2 циклів синусоїди
time = np.linspace(0, 4 * np.pi, 100)
#Переробка вибірки. Необхідний для переробки числового ряду на синусоїду в майбутньому
signal = np.sin(time) + 0.1 * np.random.normal(size=len(time))

#Маштабованість данних до стану від 0 до 1
scaler = MinMaxScaler()
signalScaled = scaler.fit_transform(signal.reshape(-1, 1)).flatten()

print(signalScaled)

#Створення масиву маски станів від 0 до 1. Потім переробка до булевого масиву, де значення менші за 0.2 - True 
mask = np.random.rand(len(signalScaled)) < 0.2  

#Копія масиву з маштабованими даними з відміною привязки
signalMissing = signalScaled.copy()

#Заміна значення маски True до np.nan для імітації розриву
signalMissing[mask] = np.nan
#Заміна значення маски np.nan до 0 для імітації розриву
inputSignal = np.nan_to_num(signalMissing, nan=0.0)

#Нейромережа автоекодера
#Вхідна боєголовка
input_layer = Input(shape=(1,))
#Енкодер
encoded = Dense(8, activation='relu')(input_layer)
#Ботлнек(звуження мережі)
encoded = Dense(4, activation='relu')(encoded)
#Декодер
decoded = Dense(8, activation='relu')(encoded)
#Вихід
output_layer = Dense(1)(decoded)

#Підготовка активації мережі
autoencoder = Model(input_layer, output_layer)
autoencoder.compile(optimizer='adam', loss='mse')


Xtrain = inputSignal.reshape(-1, 1)
Ytrain = signalScaled.reshape(-1, 1)

#Навчання моделі
autoencoder.fit(Xtrain, Ytrain, epochs=200, verbose=0)

#Ініціалізація масиву з прогнозованими данними
reconstructed = autoencoder.predict(Xtrain).flatten()

#Заміна всіх непропущених значень на значення маски
reconstructed[~mask] = signalScaled[~mask] 

# Відновлення через інтерполяцію сплайн
xknown = np.where(~mask)[0]
yknown = signalScaled[~mask]
splineInterp = UnivariateSpline(xknown, yknown, s=0)
splineFilled = signalMissing.copy()
splineFilled[mask] = splineInterp(np.where(mask)[0])

# Відновлення через інтерполяцію поліном (кубічний)
polyInterp = interp1d(xknown, yknown, kind='cubic', fill_value="extrapolate")
polyFilled = signalMissing.copy()
polyFilled[mask] = polyInterp(np.where(mask)[0])

# Обчислення середньоквадратичної похибки
truevals = signalScaled[mask]
mseAutoencoder = mean_squared_error(truevals, reconstructed[mask])
mseSpline = mean_squared_error(truevals, splineFilled[mask])
msePoly = mean_squared_error(truevals, polyFilled[mask])

# Вивід графіка
plt.figure(figsize=(12, 6))
plt.plot(signalScaled, label='Original', alpha=0.5)
plt.plot(signalMissing, 'k--', label='Missing data', alpha=0.3)
plt.plot(reconstructed, label='Autoencoder')
plt.plot(splineFilled, label='Spline Interpolation')
plt.plot(polyFilled, label='Polynomial Interpolation')
plt.legend()
plt.title("Відновлення пропущених даних у часовому ряді")
plt.show()
