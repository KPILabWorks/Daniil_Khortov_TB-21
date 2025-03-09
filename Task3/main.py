import numpy as np
from run import calculateEnergyConsumption
import time
startTime = time.time()

np.random.seed(492)
power = np.random.uniform(100, 10000, (1000, 1000))  
timeEnergy = np.random.uniform(1, 24, (1000, 1000))  

energyConsumption = calculateEnergyConsumption(power, timeEnergy)

print("Сумарне споживання енергії:", np.sum(energyConsumption), "Вт*год")
print("--- %s seconds ---" % (time.time() - startTime))