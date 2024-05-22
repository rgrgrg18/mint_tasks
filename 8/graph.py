import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

with open("./settings.txt", "r") as settings_file:
    settings_data = [float(num) for num in settings_file.read().split("\n")]

time_step = settings_data[0]
volt_step = settings_data[1]

cnt = 0
x_data = []
y_data = []
with open("./data.txt", "r") as f:
    for line in f.readlines():
        y = float(line)
        x_data.append(float(cnt*time_step))
        y_data.append(y * volt_step)
        cnt += 1

xs = np.array(x_data)
ys = np.array(y_data)

_, ax = plt.subplots(figsize=(10, 10))
ax.set_xlabel("Время, с", fontweight="bold")
ax.set_ylabel("Напряжение, В", fontweight="bold")
ax.set_title("Процесс заряда и разряда конденсатора в RC-цепочке", fontweight="bold")

my_plot = plt.plot(xs, ys, color='c', label="Зависимость напряжения от врмени U(t)",marker = 'o',
                           markerfacecolor='tab:pink',
                           markeredgecolor='m', markevery=10)

ax.xaxis.set_major_locator(ticker.MaxNLocator(10))
ax.xaxis.set_minor_locator(ticker.MaxNLocator(10))
ax.yaxis.set_major_locator(ticker.MaxNLocator(10))
ax.yaxis.set_minor_locator(ticker.MaxNLocator(10))

plt.grid(color="pink", visible=True, which='major',axis='both',alpha=1, linestyle = ":")
plt.grid(color="pink", visible=True, which='minor',axis='both',alpha=1, linestyle = ":")

plt.legend()
plt.show()
plt.savefig("8_graph.svg")