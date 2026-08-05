import matplotlib.pyplot as plt
import numpy as np

IB_TYP = 20

def data():
    # model dist of I_B1 and I_B2
    std = IB_TYP/2 #because typical more important than minmax imo
    I_B1 = np.random.normal(0, std, 100000)
    I_B2 = np.random.normal(0, std, 100000)
    plt.hist(I_B1, bins=100, color = "Green")
    plt.hist(I_B2, bins=100, color = "Purple")
    plt.show()
    #calculate I_ib and I_io 
    return I_B1, I_B2


def I_ib_gen(I_B1, I_B2):
    rng = np.random.default_rng()
    I_ib=[]
    for i in I_B1:
        I_ib.append((i + rng.choice(I_B2))/2)


    plt.hist(I_ib, bins=100, color="purple")
    plt.show()
    return I_ib


def main():
    I_B1, I_B2 = data()
    I_ib_gen(I_B1, I_B2)

if __name__ == "main":
    main()