import matplotlib.pyplot as plt
import numpy as np
import random

# X and Y axis value.
x = np.array([_ for _ in range(1, 101)])
y1 = np.array([random.randint(0, 100) for _ in range(100)])
y2 = np.array([_ for _ in range(1, 101)])
y3 = np.array([random.randint(0, 100) for _ in range(100)])
# Graph size.
plt.figure(figsize=(100, 30))
# Plot.
plt.plot(x, y1, label="Root 1", linewidth=6, color="red")
plt.plot(x, y2, label="Root 2", linewidth=6, color="green")
plt.plot(x, y3, label="Root 3", linewidth=6, color="blue")
# Show the Legend.
plt.legend(prop={"size": 50})
# Title.
plt.title('Titlu', fontsize=80)
# X and Y axis name.
plt.xlabel('Loops', fontsize=60)
plt.ylabel('Response Time', fontsize=60)
# Show all values for both x, and y.
plt.xticks(x, fontsize=30)
plt.yticks(y1, fontsize=20)
plt.yticks(y2, fontsize=20)
plt.yticks(y3, fontsize=20)
# Save the plot into a file.
plt.savefig("/home/paul/Desktop/da.png")


