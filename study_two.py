import matplotlib.pyplot as plt
import numpy as np

IB_TYP = 20
input_bias_typ = 20
input_offset_typ = 2


def dist_gen():
    std_c_I = input_bias_typ / 2
    c_I = -(np.random.gamma(1.2, std_c_I, 100000))  # one side, negative only
    std_d_I = input_offset_typ / 2
    d_I = np.random.normal(0, std_d_I, 100000)

    # Plot c(I)
    weights_c = np.ones_like(c_I) * 100.0 / len(c_I)
    plt.figure(figsize=(9, 7))
    plt.hist(c_I, bins=np.arange(-50, 2, 2), weights=weights_c, edgecolor="black")
    print("TASK cI")
    print("mean = " + str(np.mean(c_I)))
    print("std = " + str(np.std(c_I)))
    print("max = " + str(np.max(c_I)))
    print("min = " + str(np.min(c_I)))
    print("typical = " + str(2 * np.std(c_I)))
    print("MINMAX = " + str(4 * np.std(c_I)))
    plt.title("c(I) Distribution")
    plt.xlabel("Current (nA)")
    plt.ylabel("Percentage (%)")
    plt.ylim(0, 20)
    plt.grid(axis = "y", alpha = 0.1)
    plt.yticks(range(0, 25, 5))
    plt.xticks(np.arange(-50, 2, 4), rotation = "vertical")
    plt.show()

    weights_d = np.ones_like(d_I) * 100.0 / len(d_I)
    plt.figure(figsize=(9, 7))
    plt.hist(d_I, bins=np.arange(-6, 6.5, 0.5), weights=weights_d, edgecolor="black")
    print("TASK dI")
    print("mean = " + str(np.mean(d_I)))
    print("std = " + str(np.std(d_I)))
    print("max = " + str(np.max(d_I)))
    print("min = " + str(np.min(d_I)))
    print("typical = " + str(2 * np.std(d_I)))
    print("MINMAX = " + str(4 * np.std(d_I)))
    plt.title("d(I) Distribution")
    plt.xlabel("Current (nA)")
    plt.ylabel("Percentage (%)")
    plt.ylim(0, 20)
    plt.grid(axis = "y", alpha = 0.1)
    plt.yticks(range(0, 25, 5))
    plt.xticks(np.arange(-3.5, 4, 0.5), rotation="vertical")
    plt.xlim(-3.5, 3.5)
    plt.show()

    return c_I, d_I


def data(c_I, d_I):
    I_B1 = c_I + (d_I / 2)
    I_B2 = c_I - (d_I / 2)

    bins = np.arange(-50, 2, 2)
    weights_B1 = np.ones_like(I_B1) * 100.0 / len(I_B1)
    weights_B2 = np.ones_like(I_B2) * 100.0 / len(I_B2)
    plt.figure(figsize=(9, 7))
    plt.hist(I_B2, bins=bins, label="I_B2", weights=weights_B2, edgecolor="black")
    plt.title("B2 Input Currents")
    plt.xlabel("Current (nA)")
    plt.ylabel("Percentage (%)")
    plt.grid(axis = "y", alpha = 0.1)
    plt.xticks(np.arange(-50, 2, 4), rotation = "vertical")
    plt.ylim(0, 20)
    plt.yticks(range(0, 25, 5))
    plt.show()

    plt.figure(figsize=(9, 7))
    plt.hist(I_B1, bins=bins, label="I_B1", weights=weights_B1, edgecolor="black")
    plt.title("B1 Input Currents")
    plt.xlabel("Current (nA)")
    plt.ylabel("Percentage (%)")
    plt.xticks(np.arange(-50, 0, 4),rotation='vertical')
    plt.grid(axis = "y", alpha = 0.1)
    plt.ylim(0, 20)
    plt.yticks(range(0, 25, 5))
    plt.show()

    return I_B1, I_B2


def I_ib_gen(I_B1, I_B2):
    
    I_io = I_B1 - I_B2
    I_ib = (I_B1 + I_B2) / 2

    print("TASK I_IO")
    print("mean = " + str(np.mean(I_io)))
    print("std = " + str(np.std(I_io)))
    print("max = " + str(np.max(I_io)))
    print("min = " + str(np.min(I_io)))
    print("typical = " + str(2 * np.std(I_io)))
    print("MINMAX = " + str(4 * np.std(I_io)))

    print("TASK I_IB")
    print("mean = " + str(np.mean(I_ib)))
    print("std = " + str(np.std(I_ib)))
    print("max = " + str(np.max(I_ib)))
    print("min = " + str(np.min(I_ib)))
    print("typical = " + str(2 * np.std(I_ib)))
    print("MINMAX = " + str(4 * np.std(I_ib)))

    bins_ib = np.arange(-50, 2, 2)
    weights_ib = np.ones_like(I_ib) * 100.0 / len(I_ib)
    plt.figure(figsize=(9, 7))
    plt.hist(I_ib, bins=bins_ib, weights=weights_ib, edgecolor="black")
    plt.title("I_IB Distribution (Bias Current)")
    plt.xlabel("Current (nA)")
    plt.ylabel("Percentage (%)")
    plt.ylim(0, 20)
    plt.grid(axis = "y", alpha = 0.1)
    plt.yticks(range(0, 25, 5))
    plt.xticks(np.arange(-50, 2, 4), rotation = "vertical")
    plt.show()

    bins_io = np.arange(-6, 6.5, 0.5)
    weights_io = np.ones_like(I_io) * 100.0 / len(I_io)
    plt.figure(figsize=(9, 7))
    plt.hist(I_io, bins=bins_io, weights=weights_io, edgecolor="black")
    plt.title("I_IO Distribution (Offset Current)")
    plt.xlabel("Current (nA)")
    plt.grid(axis = "y", alpha = 0.1)
    plt.ylabel("Percentage (%)")
    plt.ylim(0, 20)
    plt.grid(axis = "y", alpha = 0.1)
    plt.yticks(range(0, 25, 5))
    plt.xticks(np.arange(-3.5, 4, 0.5), rotation="vertical")
    plt.xlim(-4, 4)
    plt.show()

    return I_ib, I_io


def corr(I_B1, I_B2):
    print("Correlation coefficient:", np.corrcoef(I_B1, I_B2)[0, 1])


def main():
    plt.rc('axes.spines', top=False, right=False, left=True, bottom=True)
    I_c, I_d = dist_gen()
    I_B1, I_B2 = data(I_c, I_d)
    I_ib_gen(I_B1, I_B2)
    corr(I_B1, I_B2)


if __name__ == "__main__":
    main()