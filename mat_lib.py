import matplotlib.pyplot as plt
import numpy as np
import keyword

path = "/home/paul/Desktop/da.png"


@keyword("PLOT")
def plot(lst1, lst2, lst3, loops):
    # X and Y axis value.
    x = np.array(list(range(loops)))
    y1 = np.array([_ for _ in lst1])
    y2 = np.array([_ for _ in lst2])
    y3 = np.array([_ for _ in lst3])
    # Graph size.
    length = len(loops)
    plt.figure(figsize=(length // 2, length // 6))
    # Plot.
    plt.plot(x, y1, label="Route 1", linewidth=6, color="red")
    plt.plot(x, y2, label="Route 2", linewidth=6, color="green")
    plt.plot(x, y3, label="Route 3", linewidth=6, color="blue")
    # Show the Legend.
    plt.legend(prop={"size": 50}, loc="upper left")
    # Title.
    plt.title('RESPONSE_TIME_TC', fontsize=80)
    # X and Y axis name.
    plt.xlabel("Iterations", fontsize=60)
    plt.ylabel("Response Time", fontsize=70)
    # Show all values for both x, and y.
    plt.xticks(fontsize=40)
    plt.yticks(fontsize=40)
    # Save the plot into a file.
    plt.savefig(path)
