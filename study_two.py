import matplotlib.pyplot as plt
import numpy as np

IB_TYP = 20


def data():
    # model dist of I_B1 and I_B2
    std = IB_TYP / 2  # because typical more important than minmax imo
    I_B1 = np.random.normal(0, std, 100000)
    I_B2 = np.random.normal(0, std, 100000)
    plt.hist(I_B1, bins=1 + int(np.log2(len(I_B1))), color="Green")
    plt.hist(I_B2, bins=1 + int(np.log2(len(I_B2))), color="Purple")
    plt.show()
    # calculate I_ib and I_io
    return I_B1, I_B2


def I_ib_gen(I_B1, I_B2):
    rng = np.random.default_rng()
    I_io = []
    for i in I_B1:
        I_io.append(i - rng.choice(I_B2))  # multiply each I_B1 with a random I_B2
    print("TASK I_IO")
    print("mean = " + str(np.mean(I_io)))
    print("std = " + str(np.std(I_io)))
    print("max = " + str(np.max(I_io)))
    print("min = " + str(np.min(I_io)))
    print("typical = " + str(2 * np.std(I_io)))
    print("MINMAX = " + str(4 * np.std(I_io)))
    plt.hist(I_io, bins=1 + int(np.log2(len(I_io))), color="green")
    I_ib = []
    for i in I_B1:
        I_ib.append((i + rng.choice(I_B2)) / 2)  # multiply each I_B1 with a random I_B2
    print("TASK I_IB")
    print("mean = " + str(np.mean(I_ib)))
    print("std = " + str(np.std(I_ib)))
    print("max = " + str(np.max(I_ib)))
    print("min = " + str(np.min(I_ib)))
    print("typical = " + str(2 * np.std(I_ib)))
    print("MINMAX = " + str(4 * np.std(I_ib)))
    plt.hist(I_ib, bins=1 + int(np.log2(len(I_ib))), color="purple")
    plt.show()
    return I_ib


def main():
    I_B1, I_B2 = data()
    I_ib_gen(I_B1, I_B2)


if __name__ == "__main__":
    main()
