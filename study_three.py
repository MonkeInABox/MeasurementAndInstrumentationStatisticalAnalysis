import matplotlib.pyplot as plt
import numpy as np

TYP = 10

# PART A
"""
Generate 10^5 values to create dataset for OPA445AP
Get mean, std, max, min
Create histogram
"""


def data():
    std = TYP / 2  # because typical more important than minmax imo
    # std = (MINMAX/4)
    dataset = 9 * np.random.weibull((std / 2) / TYP + 1, 10000000)
    print("mean = " + str(np.mean(dataset)))
    print("std = " + str(np.std(dataset)))
    print("max = " + str(np.max(dataset)))
    print("min = " + str(np.min(dataset)))
    print("typical = " + str(2 * np.std(dataset)))
    print("MINMAX = " + str(4 * np.std(dataset)))
    plt.hist(dataset, bins=100)
    plt.show()
    return dataset


def dataPW():
    std = TYP / 2  # because typical more important than minmax imo
    # std = (MINMAX/4)
    dataset = np.linspace(0, 40, 10000)
    cond = [
        (0 < dataset) & (dataset < 2),
        2 <= dataset < 4,
        4 <= dataset < 6,
        6 <= dataset < 8,
        8 <= dataset < 10,
        10 <= dataset < 12,
        12 <= dataset < 14,
        14 <= dataset < 16,
        16 <= dataset < 18,
        18 <= dataset < 20,
        20 <= dataset < 22,
        22 <= dataset < 24,
        24 <= dataset < 26,
        26 <= dataset < 28,
        28 <= dataset < 30,
        30 <= dataset < 32,
        32 <= dataset < 34,
        34 <= dataset < 36,
        36 <= dataset < 38,
        38 <= dataset < 40,
    ]
    for i in range(0, 40, 2):
        cond.append((i) < dataset < (i + 2))
    func = [
        0.10,
        0.24,
        0.14,
        0.14,
        0.11,
        0.075,
        0.052,
        0.051,
        0.04,
        0.015,
        0.02,
        0.015,
        0.01,
        0.005,
        0.008,
        0.005,
        0.005,
        0.005,
        0.005,
        0,
    ]
    np.piecewise(dataset, cond, func)
    print("mean = " + str(np.mean(dataset)))
    print("std = " + str(np.std(dataset)))
    print("max = " + str(np.max(dataset)))
    print("min = " + str(np.min(dataset)))
    print("typical = " + str(2 * np.std(dataset)))
    print("MINMAX = " + str(4 * np.std(dataset)))
    plt.hist(dataset, bins=100)
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
    mask = dataset >= -0
    dataset = dataset[mask]
    print("TASK 1B")
    print("mean = " + str(np.mean(dataset)))
    print("std = " + str(np.std(dataset)))
    print("max = " + str(np.max(dataset)))
    print("min = " + str(np.min(dataset)))
    print("typical = " + str(2 * np.std(dataset)))
    print("MINMAX = " + str(4 * np.std(dataset)))
    plt.hist(dataset, bins=range(0, 40, 2), color="green")
    plt.xticks(range(0, 40, 2))
    plt.show()
    return 0


def main():
    dataPW()
    dataset = data()
    sort(dataset)


if __name__ == "__main__":
    main()
