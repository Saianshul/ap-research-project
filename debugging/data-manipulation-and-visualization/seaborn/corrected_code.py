import seaborn as sns
import matplotlib.pyplot as plt

flights = sns.load_dataset("flights")

sns.set_theme(style="dark")

g = sns.relplot(data=flights, x="month", y="passengers", col="year", hue="year", kind="line", palette="magma", zorder=3, col_wrap=3, height=2, legend=False)

for ax in g.axes.flat:
    year = ax.get_title().split('=')[1].strip()
    ax.text(.2, .8, year, transform=ax.transAxes, fontweight="bold")
    ax.grid(True)

g.fig.suptitle("Monthly Passengers (1949-1960)")
g.set_titles("")
g.set_axis_labels("", "Passengers")

plt.show()

fig, ax = plt.subplots(figsize=(9, 7))
flights_pivot = flights.pivot("month", "year", "passengers")
sns.heatmap(flights_pivot, annot=True, fmt="d", cmap="coolwarm", ax=ax)

plt.show()