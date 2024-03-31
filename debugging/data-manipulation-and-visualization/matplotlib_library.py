import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import datetime
import numpy as np

events = ["V J Day", "Truman Doctrine", "Marshall Plan", "Berlin Blockade", "NATO", "Start of Korean War", "Death of Stalin", "End of Korean War", "Warsaw Pact", "Hungarian Revolution", "Berlin Wall", "Cuban Missile Crisis", "JFK Assassination", "SALT", "End of Vietnam War", "Fall of the Berlin Wall", "Reunification of Germany", "End of the Soviet Union"]

str_dates = ["1945-08-14", "1947-03-12", "1947-06-05", "1948-06-24", "1949-04-04", "1950-06-25", "1953-03-05", "1953-07-27", "1955-05-14", "1956-10-23", "1961-08-13", "1962-10-14", "1963-11-22", "1972-05-26", "1975-04-30", "1989-11-9", "1990-10-03", "1991-12-26"]
dates = []
for date in str_dates:
    datetime_object = datetime.strptime(date, "%Y-%m-%d")
    dates.append(datetime_object)

vline_heights = np.tile([-4, 4, -3, 3, -2, 2], len(dates))[:len(dates)]

fig, ax = plt.subplots(figsize=(10, 5), layout="constrained")
ax.set(title="Cold War Timeline")

# ax.vlines(dates, 0, vline_heights, color="tab:blue")
ax.plot(dates, "-o", color="k", markerfacecolor="w")
# ax.plot(dates, np.zeros_like(dates), "-o", color="k", markerfacecolor="w")

for date, height, event in zip(dates, vline_heights, events):
    if height <= 0:
        vertical_alignment = "top"
    else:
        vertical_alignment = "bottom"
        
    ax.annotate(event, xy=(date, height), xytext=(-3, np.sign(height)*3), textcoords="offset points", horizontalalignment="center", verticalalignment=vertical_alignment)

ax.xaxis.set_major_locator(mdates.MonthLocator(interval=10))
ax.xaxis.set_major_formatter(mdates.DateFormatter("%b %Y"))
plt.setp(ax, rotation=30, ha="right")
# plt.setp(ax.get_xticklabels(), rotation=30, ha="right")

ax.yaxis.set_visible(False)
ax.spines[["left", "top", "right"]].set_visible(False)

plt.show()