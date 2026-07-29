import numpy as np
import matplotlib as plot

# PART A
"""
Generate 10^5 values to create dataset for OPA445AP
Get mean, std, max, min
Create histogram
"""
def data():
    dataset = np.random.uniform(0, 3, 100000)
    print("mean = " + str(np.mean(dataset)))
    print("std = " + str(np.std(dataset)))
    print("max = " + str(np.max(dataset)))
    print("min = " + str(np.min(dataset)))
    return 0

# PART B
"""
Extract samples to specify in datasheet that we have OA with a typical value of 1mV and a max of 3mV
Statistics and number with this higher performance
Statistics and number of other
Histograms
"""
def sort():
    return 0

def main():
    data()
    sort()

if __name__ == "__main__":
    main()


""""
THIS IS A TEST. POOPY FART
""""