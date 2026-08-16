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
    std = TYP / 2  # because typical more important than minmax iao
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
    edges = np.arange(0, 42, 2)  # bin boundaries
    func = [  # probabilities per bin (estimated visually from datasheet)
        0.10,
        0.24,
        0.14,
        0.14,
        0.11,
        0.075,
        0.05,
        0.05,
        0.04,
        0.01,
        0.014,
        0.01,
        0.007,
        0.002,
        0.004,
        0.002,
        0.002,
        0.002,
        0.002,
        0,
    ]

    num_samples = 100000
    bin_indices = np.random.choice(len(func), size=num_samples, p=func)

    dataset = np.array([np.random.uniform(edges[i], edges[i + 1]) for i in bin_indices])
    mean_val = np.mean(dataset)
    std_val = np.std(dataset)
    typical = 2 * std_val
    minmax = 4 * std_val
    print("mean = " + str(mean_val))
    print("std = " + str(std_val))
    print("max = " + str(np.max(dataset)))
    print("min = " + str(np.min(dataset)))
    print("typical = " + str(typical))
    print("MINMAX = " + str(minmax))
    plt.figure(figsize=(10, 5))
    plt.hist(dataset, bins=edges)
    plt.title("Sampled Piecewise Histogram Distribution")
    plt.xlabel("Offset Voltage Drift (uV/°C)")
    plt.ylabel("Frequency")
    plt.grid(axis="y", linestyle="--", alpha=0.7)
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
