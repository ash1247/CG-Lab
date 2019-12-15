import numpy as np
import matplotlib.pyplot as plt

nodes = 20

# numpy.arange([start, ]stop, [step, ]dtype=None)
# Return evenly spaced values within a given interval.
x = np.arange(0, nodes, 0.1)
# creates cosine value of the given x value
cos_curve = np.cos(x)
# creates sine value of the given x value
sin_curve = np.sin(x)
# creates tangent value of the given x value
tan_curve = np.tan(x)

plt.title("Sine, Cosine, Tangent Curve")
plt.subplot(3, 1, 1)
plt.plot(x, sin_curve)
plt.ylabel("sin(x)")

plt.subplot(3, 1, 2)
plt.plot(x, cos_curve)
plt.ylabel("cos(x)")

plt.subplot(3, 1, 3)
plt.plot(x, tan_curve)
plt.ylabel("tan(x)")
plt.xlabel("x")

plt.show()
