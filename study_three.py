import matplotlib.pyplot as plt
import numpy as np

TYP = 10

# PART A
"""
Generate 10^5 values to create dataset for OPA445AP
Get mean, std, max, min
Create histogram
"""


# def data():
#     std = TYP / 2  # because typical more important than minmax iao
#     # std = (MINMAX/4)
#     dataset = 9 * np.random.weibull((std / 2) / TYP + 1, 10000000)
#     print("mean = " + str(np.mean(dataset)))
#     print("std = " + str(np.std(dataset)))
#     print("max = " + str(np.max(dataset)))
#     print("min = " + str(np.min(dataset)))
#     print("typical = " + str(2 * np.std(dataset)))
#     print("MINMAX = " + str(4 * np.std(dataset)))
#     plt.hist(dataset, bins=100)
#     plt.show()
#     return dataset


def dataPW():
    edges = np.arange(0.1, 40, 2)  # bin boundaries
    func = [  # probabilities per bin (estimated visually from datasheet)
        0.10,
        0.24,
        0.14,
        0.14,
        0.11,
        0.065,
        0.05,
        0.05,
        0.04,
        0.01,
        0.024,
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
    weights = np.ones_like(dataset) * (100.0 / len(dataset))
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
    plt.figure(figsize=(9, 7))
    plt.hist(dataset, bins=edges, weights=weights, edgecolor = 'black', color="teal")
    plt.grid(axis = "y", alpha = 0.1)
    plt.title("Sampled Piecewise Histogram Distribution")
    plt.xlabel("Offset Voltage Drift (uV/°C)")
    plt.ylabel("Frequency (%)")
    plt.xticks(range(0, 42, 2))
    plt.yticks(np.arange(0, 27.5, 2.5))
    plt.show()
    log_samples = np.log(dataset)
    mu = np.mean(log_samples)
    sigma = np.std(log_samples)
    logs = np.random.lognormal(mu, sigma, 100000)
    logs = np.clip(logs, a_min=0, a_max=45)
    weights_log = np.ones_like(logs) * (100.0 / len(logs))
    mean_log = np.mean(logs)
    std_log = np.std(logs)
    typical = std_log * 2
    minmax = std_log * 4
    print("LOG")
    print("mean = " + str(mean_log))
    # print("true mean = " + str(np.exp(mu+(sigma**2)/2)))
    print("std = " + str(std_log))
    print("max = " + str(np.max(logs)))
    print("min = " + str(np.min(logs)))
    print("typical = " + str(typical))
    print("MINMAX = " + str(minmax))
    plt.figure(figsize=(9, 7))
    plt.hist(logs, bins = edges, weights=weights_log, edgecolor = 'black', color="teal")
    plt.grid(axis = "y", alpha = 0.1)
    plt.title("Log Normal Fit Histogram Distribution")
    plt.xlabel("Offset Voltage Drift (uV/°C)")
    plt.ylabel("Frequency (%)")
    plt.xticks(range(0, 42, 2))
    plt.yticks(np.arange(0, 27.5, 2.5))
    plt.show()

    return dataset, logs


# PART B
"""
Extract samples to specify in datasheet that we have OA with a typical value of 1mV and a max of 3mV
Statistics and number with this higher performance
Statistics and number of other
Histograms
"""


# def sort(dataset):
#     mask = dataset >= -0
#     dataset = dataset[mask]
#     print("TASK 1B")
#     print("mean = " + str(np.mean(dataset)))
#     print("std = " + str(np.std(dataset)))
#     print("max = " + str(np.max(dataset)))
#     print("min = " + str(np.min(dataset)))
#     print("typical = " + str(2 * np.std(dataset)))
#     print("MINMAX = " + str(4 * np.std(dataset)))
#     plt.hist(dataset, bins=range(0, 42, 2), color="green")
#     plt.xticks(range(0, 42, 2))
#     plt.show()
#     return 0

def data():
    TYP = 1.5
    std = TYP / 2  # because typical more important than minmax imo
    # std = (MINMAX/4)
    dataset = np.random.normal(0, std, 100000)
    weights = np.ones_like(dataset) * (100.0 / len(dataset))
    print("mean = " + str(np.mean(dataset)))
    print("std = " + str(np.std(dataset)))
    print("max = " + str(np.max(dataset)))
    print("min = " + str(np.min(dataset)))
    print("typical = " + str(2 * np.std(dataset)))
    print("MINMAX = " + str(4 * np.std(dataset)))
    plt.figure(figsize=(9, 7))
    plt.hist(dataset, bins=np.arange(-3, 3, 0.2), weights=weights, edgecolor="black", color="teal")
    plt.grid(axis = "y", alpha = 0.1)
    plt.xticks(np.arange(-3, 3, 0.4),rotation='vertical')
    plt.yticks(np.arange(0, 12, 1))
    plt.ylim(0, 12)
    plt.title("Original Input Offset Voltage Simulation")
    plt.xlabel("Voltage V")
    plt.yticks(np.arange(0, 27.5, 2.5))
    plt.ylabel("Frequency (% of Original Dataset)")
    plt.show()
    return dataset

def offset(vos_25, drift_dataset):
    sign = np.random.choice([-1, 1], size=100000)
    drift_signed = sign * drift_dataset 

    dT_max = 85 - 25
    dT_min = -25 - 25  
    max = vos_25 + (drift_signed * dT_max) / 1000.0
    min = vos_25 + (drift_signed * dT_min) / 1000.0

    print("Normal")
    print("mean =", np.mean(vos_25))
    print("std =", np.std(vos_25))
    print("max =", np.max(vos_25))
    print("min =", np.min(vos_25))

    print("MAX")
    print("mean =", np.mean(max))
    print("std =", np.std(max))
    print("max =", np.max(max))
    print("min =", np.min(max))

    print("MIN")
    print("mean =", np.mean(min))
    print("std =", np.std(min))
    print("max =", np.max(min))
    print("min =", np.min(min))

    bins = np.arange(-4, 4.5, 0.5)
    weights_max = np.ones_like(max) * (100.0 / len(max))
    weights_min = np.ones_like(min) * (100.0 / len(min))

    plt.figure(figsize=(9, 7))
    plt.hist(max, bins=bins, weights=weights_max, edgecolor="black", color="teal")
    plt.grid(axis = "y", alpha = 0.1)
    plt.title("Offset Voltage at Maximum Temperature (85°C )")
    plt.xlabel("Offset Voltage (mV)")
    plt.yticks(np.arange(0, 27.5, 2.5))
    plt.ylabel("Frequency (%)")
    plt.show()

    plt.figure(figsize=(9, 7))
    plt.hist(min, bins=bins, weights=weights_min, edgecolor="black", color="teal")
    plt.grid(axis = "y", alpha = 0.1)
    plt.title("Offset Voltage at Minimum Temperature (-20°C )")
    plt.xlabel("Offset Voltage (mV)")
    plt.ylabel("Frequency (%)")
    plt.yticks(np.arange(0, 27.5, 2.5))
    plt.show()

    return max, min

def main():
    plt.rc('axes.spines', top=False, right=False, left=True, bottom=True)
    dataset = data()
    ___, logs = dataPW()
    offset(dataset, logs)

    #dataset = data()
    #sort(dataset)


if __name__ == "__main__":
    main()