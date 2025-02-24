import pandas as pd
from joblib import Memory
import time
import numpy as np


def generate_dataset(filename, num_rows=1_000_000):
    print("Generating dataset...")
    data = {
        "a": np.random.randint(1, 100, size=num_rows),
        "b": np.random.randint(1, 100, size=num_rows)
    }
    df = pd.DataFrame(data)
    df.to_csv(filename, index=False)
    print(f"Dataset saved to {filename}")



def import_dataset(filename):
    print("Importing dataset...")
    return pd.read_csv(filename)


memory = Memory("./cache", verbose=0)



@memory.cache
def someHeavyMathFormula(data):
    print("Performing heavy computation...")
    time.sleep(3)
    df = data.copy()
    df["sum"] = df["a"] + df["b"]
    return df


if __name__ == "__main__":
    filename = "dataset.csv"


    generate_dataset(filename)


    data = import_dataset(filename)

    print("Computation 1: ")
    result1 = someHeavyMathFormula(data)
    print(result1.head())  

    print("Computation 2: ")
    result2 = someHeavyMathFormula(data)
    print(result2.head())
