# IPython log file
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
x = np.linspace(0.0, 4.0, 40)
g = x**2
h = x**3
plt.plot(x, g, "y.", label = "Squared")
plt.plot(x, h, "gx", label = "Cubed")
plt.title("Squared vs Cubed")
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.legend()
plt.show()
plt.savefig("Weekly_task_8.png")

