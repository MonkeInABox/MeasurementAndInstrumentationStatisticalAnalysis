import matplotlib.pyplot as plt
import numpy as np

TYP = 1.5
MINMAX = 5
STDEV_REQ = 0.5
np.random.seed(23)

# PART A
"""
Generate 10^5 values to create dataset for OPA445AP
Get mean, std, max, min
Create histogram
"""

# generate original data
def data():
    std = TYP / 2  # because typical more important than minmax 
    # std = (MINMAX/4)
    dataset = np.random.normal(0, std, 100000)
    mask = dataset <= 3.05
    dataset = dataset[mask]
    mask = dataset >= -3.05
    dataset = dataset[mask]
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
    plt.ylabel("Frequency (% of Original Dataset)")
    plt.show()
    return dataset


# PART B
"""
Extract samples to specify in datasheet that we have OA with a typical value of 1mV and a max of 3mV
Statistics and number with this higher performance
Statistics and number of other
Histograms
"""

# old unused sort
# def sort(dataset):
#     leftover_mask = (dataset < -1.05) | (dataset > 1.05)
#     negative_ds = dataset[leftover_mask]
#     mask = dataset <= 1.05
#     dataset = dataset[mask]
#     mask = dataset >= -1.05
#     dataset = dataset[mask]

#     print("TASK 1B")
#     print("mean = " + str(np.mean(dataset)))
#     print("std = " + str(np.std(dataset)))
#     print("max = " + str(np.max(dataset)))
#     print("min = " + str(np.min(dataset)))
#     print("typical = " + str(2 * np.std(dataset)))
#     print("MINMAX = " + str(4 * np.std(dataset)))
#     ___, bins, ___ = plt.hist(dataset, bins='rice', edgecolor = "black")
#     plt.xticks(bins)
#     plt.title("High Quality Input Offset Voltages")
#     plt.xlabel("Voltage (V)")
#     plt.ylabel("Frequency")
#     plt.show()

#     print("TASK 1B")
#     print("mean = " + str(np.mean(negative_ds)))
#     print("std = " + str(np.std(negative_ds)))
#     print("max = " + str(np.max(negative_ds)))
#     print("min = " + str(np.min(negative_ds)))
#     print("typical = " + str(2 * np.std(negative_ds)))
#     print("MINMAX = " + str(4 * np.std(negative_ds)))
#     ___, bins, ___ = plt.hist(negative_ds, bins=np.arange(-3.05, 3.05, 0.1), edgecolor = "black")
#     plt.xticks(np.arange(-3, 3, 0.4),rotation='vertical')
#     plt.title("Low Quality Input Offset Voltages")
#     plt.xlabel("Voltage (V)")
#     plt.ylabel("Frequency")
#     plt.show()

#     return 0

def sort_new(dataset):
    total_original_count = len(dataset)
    ratio = (TYP/2) / STDEV_REQ

    # adapted from https://www.geeksforgeeks.org/python/how-to-plot-a-normal-distribution-with-matplotlib-in-python/
    sampling = ratio * (1 / ((TYP/2) * np.sqrt(2 * np.pi))) * np.exp(-0.5 * (dataset / (TYP/2)) ** 2)
    u = np.random.uniform(0, sampling)
    # adapted from https://agdenadel.github.io/Rejection-sampling/
    target = (1 / (STDEV_REQ * np.sqrt(2 * np.pi))) * np.exp(-0.5 * (dataset / STDEV_REQ) ** 2)

    accept = u <= target

    good = dataset[accept]
    bad = dataset[~accept]

    good = good[(good <= 3.05) & (good >= -3.05)]
    bad = bad[(bad <= 3.05) & (bad >= -3.05)]
    # mask = bad <= 1.1
    # bad = bad[mask]
    # mask = bad >= -1.1
    # bad = bad[mask]

    print("ACCEPT")
    print("mean = " + str(np.mean(good)))
    print("std = " + str(np.std(good)))
    print("max = " + str(np.max(good)))
    print("min = " + str(np.min(good)))
    print("typical = " + str(2 * np.std(good)))
    print("MINMAX = " + str(4 * np.std(good)))
    good_weights = np.ones_like(good) * (100.0 / total_original_count)
    plt.figure(figsize=(9, 7))
    plt.hist(good, bins=np.arange(-3, 3, 0.2), weights=good_weights, edgecolor="black", color="teal")
    plt.xticks(np.arange(-3, 3, 0.4), rotation='vertical')
    plt.yticks(np.arange(0, 12, 1))
    plt.ylim(0, 12)
    plt.grid(axis="y", alpha=0.1)
    plt.title("High Quality Input Offset Voltages")
    plt.xlabel("Voltage (V)")
    plt.ylabel("Frequency (% of Original Dataset)")
    print("length = " + str(len(good)))
    plt.show()

    print("REJECT")
    print("mean = " + str(np.mean(bad)))
    print("std = " + str(np.std(bad)))
    print("max = " + str(np.max(bad)))
    print("min = " + str(np.min(bad)))
    print("typical = " + str(2 * np.std(bad)))
    print("MINMAX = " + str(4 * np.std(bad)))
    print("length = " + str(len(bad)))
    # frequency in % 
    bad_weights = np.ones_like(bad) * (100.0 / total_original_count)
    plt.figure(figsize=(9, 7))
    plt.hist(bad, bins=np.arange(-3, 3, 0.2), weights=bad_weights, edgecolor="black", color="teal")
    plt.xticks(np.arange(-3, 3, 0.4), rotation='vertical')
    plt.yticks(np.arange(0, 12, 1))
    plt.ylim(0, 12)
    plt.grid(axis="y", alpha=0.1)
    plt.title("Low Quality Input Offset Voltages")
    plt.xlabel("Voltage (V)")
    plt.ylabel("Frequency (% of Original Dataset)")
    plt.show()

    return good, bad


def main():
    #get rid of borders
    plt.rc('axes.spines', top=False, right=False, left=True, bottom=True)
    dataset = data()
    sort_new(dataset)


if __name__ == "__main__":
    main()
