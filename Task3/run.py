import numpy as np
import time
startTime = time.time()


def calculateEnergyConsumption(powerMatrix, timeMatrix):

    if powerMatrix.shape != timeMatrix.shape:
        raise ValueError("Розміри матриць повинні співпадати")
    
    return powerMatrix * timeMatrix


np.random.seed(492) 
power = np.random.uniform(100, 10000, (10000, 1000)) 
timeEnergy = np.random.uniform(1, 24, (10000, 1000))  
    
energyConsumption = calculateEnergyConsumption(power, timeEnergy)
    
print("Сумарне споживання енергії:", np.sum(energyConsumption), "Вт*год")
print("--- %s seconds ---" % (time.time() - startTime))