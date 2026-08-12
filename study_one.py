import matplotlib.pyplot as plt
import numpy as np

TYP = 1.5
MINMAX = 5

# PART A
"""
Generate 10^5 values to create dataset for OPA445AP
Get mean, std, max, min
Create histogram
"""


def data():
    std = TYP / 2  # because typical more important than minmax imo
    # std = (MINMAX/4)
    dataset = np.random.normal(0, std, 100000)
    print("mean = " + str(np.mean(dataset)))
    print("std = " + str(np.std(dataset)))
    print("max = " + str(np.max(dataset)))
    print("min = " + str(np.min(dataset)))
    print("typical = " + str(2 * np.std(dataset)))
    print("MINMAX = " + str(4 * np.std(dataset)))
    plt.hist(dataset, bins=1 + int(np.log2(len(dataset))))
    plt.show()
    return dataset


# PART B
"""
Extract samples to specify in datasheet that we have OA with a typical value of 1mV and a max of 3mV
Statistics and number with this higher performance
Statistics and number of other
Histograms
"""


def sort(dataset):
    mask = dataset <= 1.05
    dataset = dataset[mask]
    mask = dataset >= -1.05
    dataset = dataset[mask]
    print("TASK 1B")
    print("mean = " + str(np.mean(dataset)))
    print("std = " + str(np.std(dataset)))
    print("max = " + str(np.max(dataset)))
    print("min = " + str(np.min(dataset)))
    print("typical = " + str(2 * np.std(dataset)))
    print("MINMAX = " + str(4 * np.std(dataset)))
    plt.hist(dataset, bins=1 + int(np.log2(len(dataset))))
    plt.show()
    return 0


def main():
    dataset = data()
    sort(dataset)


if __name__ == "__main__":
    main()
