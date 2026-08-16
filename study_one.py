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
    plt.title("Input Offset Voltages")
    plt.xlabel("Voltage V")
    plt.ylabel("Frequency")
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
    leftover_mask = (dataset < -1.05) | (dataset > 1.05)
    negative_ds = dataset[leftover_mask]
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
    plt.title("High Quality Input Offset Voltages")
    plt.xlabel("Voltage (V)")
    plt.ylabel("Frequency")
    plt.show()

    print("TASK 1B")
    print("mean = " + str(np.mean(negative_ds)))
    print("std = " + str(np.std(negative_ds)))
    print("max = " + str(np.max(negative_ds)))
    print("min = " + str(np.min(negative_ds)))
    print("typical = " + str(2 * np.std(negative_ds)))
    print("MINMAX = " + str(4 * np.std(negative_ds)))
    plt.hist(negative_ds, bins=1 + int(np.log2(len(negative_ds))))
    plt.title("Low Quality Input Offset Voltages")
    plt.xlabel("Voltage (V)")
    plt.ylabel("Frequency")
    plt.show()

    return 0


def main():
    dataset = data()
    sort(dataset)


if __name__ == "__main__":
    main()
