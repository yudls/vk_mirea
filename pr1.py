import matplotlib.pyplot as plt


def Amdala_pr1():
    s1 = 0.1
    s2 = 0.3
    a1 = []
    a2 = []
    for n in range(130, 1000, 10):
        a1.append(n / (n * s1 + 1 - s1))
        a2.append(n / (n * s2 + 1 - s2))
        plt.plot(a1, color='red')
        plt.plot(a2, color='blue')
    # print(a1)
    # print(a2)
    plt.show()


def Amdala_pr2():
    n1 = 100
    n2 = 200
    a1 = []
    a2 = []
    s = 0.1
    while s <= 0.5:
        a1.append(n1 / (n1 * s + 1 - s))
        a2.append(n2 / (n2 * s + 1 - s))
        plt.plot(a1, color='red')
        plt.plot(a2, color='blue')
        s += 0.005
    plt.show()


def Amdala_pr3():
    s1 = 0.1
    s2 = 0.3
    a1 = []
    a2 = []
    for n in range(130, 1000, 10):
        a1.append(n + (1 - n) * s1)
        a2.append(n + (1 - n) * s2)
        plt.plot(a1, color='red')
        plt.plot(a2, color='blue')
    plt.show()


def Amdala_pr4():
    n1 = 100
    n2 = 200
    a1 = []
    a2 = []
    s = 0.1
    while s <= 0.5:
        # for s in range(0.8, 0.7, -0.005):
        a1.append(n1 + (1 - n1) * s)
        a2.append(n2 + (1 - n2) * s)
        plt.plot(a1, color='red')
        plt.plot(a2, color='blue')
        s += 0.005
    plt.show()


if __name__ == "__main__":
    Amdala_pr1()
    Amdala_pr2()
    Amdala_pr3()
    Amdala_pr4()