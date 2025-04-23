import numpy as np
import random
import matplotlib.pyplot as plt
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression


time = np.arange('2022-01', '2025-01', np.timedelta64(1, 'M'), dtype = 'datetime64[M]')

income = np.array([random.randrange(0, 1000) + 5000+1000*k/12 for k in range(36)])
salary = np.array([(random.randrange(0, 100)+ 500)*5+500*l/12 for l in range(36)])   
electricity = np.array([(random.randrange(0, 100)+ 100) for _ in range(36)])   
heat = np.array([(random.randrange(0, 100)+ 150) for _ in range(36)])   
otherExpenses = np.array([(random.randrange(0, 100)*10) for _ in range(36)])   

profit = income - salary - electricity - heat - otherExpenses

timePoly = np.arange('2022-01', '2025-07', np.timedelta64(1, 'M'), dtype = 'datetime64[M]')

x = np.arange(0, 36, 1).reshape(-1, 1)
poly = PolynomialFeatures(degree=3, include_bias=False)
polyFeatures = poly.fit_transform(x)

model = LinearRegression()
model.fit(polyFeatures, profit)
knownProfit = model.predict(polyFeatures)


xPredict = np.arange(42).reshape(-1, 1)
xPredictPoly = poly.transform(xPredict)
predictedProfit = model.predict(xPredictPoly)

plt.figure(figsize=(14, 6))


plt.subplot(1, 2, 1)
plt.plot(time, income, label="Income", color="lime")
plt.plot(time, salary, label="Salary", color="red")
plt.plot(time, electricity, label="Electricity", color="crimson")
plt.plot(time, heat, label="Heat", color="yellow")
plt.plot(time, otherExpenses, label="Other", color="orange")
plt.plot(time, profit, label="Profit", color="green")
plt.title("Data")
plt.legend()



plt.subplot(1, 2, 2)
plt.plot(timePoly, predictedProfit, color='green', label='Predicted Profit')
plt.plot(time, profit, color='gray', label='Profit')
plt.legend()
plt.title("Profit Prediction")

plt.show()

expanses = np.column_stack([salary, electricity, heat, otherExpenses])
model = LinearRegression()
model.fit(expanses, profit)
print("Main risk Factors:")
for name, coef in zip(["Salary", "Electricity", "Heat", "Other"], model.coef_):
    print(f"{name}: {coef:.2f}")
    