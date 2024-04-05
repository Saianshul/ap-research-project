import seaborn as sns
import matplotlib.pyplot as plt

flights = sns.load_dataset("flights")

sns.set_theme(style="dark")

g = sns.relplot(data=flights, x="month", y="passengers", col="year", hue="year", kind="line", palette="magma", zorder=3, col_wrap=3, height=2, legend=False)

for year, ax in g:
# for year, ax in g.axes_dict.items():
    ax.text(.2, .8, year, transform=ax.transAxes, fontweight="bold")
    sns.lineplot(data=flights, x="month", y="passengers", units="year", estimator=None, color=".8", linestyle="--")
    # sns.lineplot(data=flights, x="month", y="passengers", units="year", estimator=None, color=".8", ax=ax, linestyle="--")
    ax.grid(True)

g.fig.suptitle("Monthly Passengers (1949-1960)")
g.set_titles("")
g.set_axis_labels("", "Passengers")

plt.show()

# flights = (flights.pivot(index="month", columns="year", values="passengers"))

fig, ax = plt.subplots(figsize=(9, 7))
sns.heatmap(flights, annot=True, fmt="d", cmap="coolwarm", ax=ax)

plt.show()