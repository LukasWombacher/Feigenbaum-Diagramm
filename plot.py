import matplotlib.pyplot as plt
import numpy as np

r_range = [2, 4]
r_resolution = 0.05
precision_integrations = 100
shown_integrations = 40
x_0 = 0.5

plt.figure()
plt.xlabel('r')
plt.ylabel('x')
plt.xlim(r_range[0], r_range[1])
plt.ylim(0, 1)
plt.grid(False)
plt.title('Feigenbaum Diagramm')

calc_progress = 0

for r_value in np.arange(r_range[0], r_range[1] + r_resolution, r_resolution):
    x = x_0
    for integration in range(0, precision_integrations):
        x = r_value * x * (1 - x)
        if integration > precision_integrations - shown_integrations:
            plt.scatter(r_value, x, color='blue', marker='o', s=1)
    new_calc_progress = int((100 / ((r_range[1] - r_range[0]) / r_resolution + 1)) * (r_value - r_range[0]) / r_resolution)
    if new_calc_progress != calc_progress:
        calc_progress = new_calc_progress
        print(str(calc_progress) + " %")

plt.get_current_fig_manager().full_screen_toggle()
plt.show()
