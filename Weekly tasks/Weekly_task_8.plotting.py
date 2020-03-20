# IPython log file
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
x = np.linspace(0.0, 4.0, 40)
g = x**2
h = x**3
plt.plot(x, x, "r.", label = "f(x) = x")
plt.plot(x, g, "y*", label = "g(x) = $x^2$")
plt.plot(x, h, "gx", label = "h(x) = $x^3$")
plt.title("Weekly_Task_8_Plotting")
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.legend()
plt.savefig("Weekly_task_8.png")
plt.show(block=False)
plt.pause(5)
plt.close("all")