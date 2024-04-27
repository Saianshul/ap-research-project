import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import datetime
import numpy as np

events = ["V J Day", "Truman Doctrine", "Marshall Plan", "Berlin Blockade", "NATO", "Start of Korean War", "Death of Stalin", "End of Korean War", "Warsaw Pact", "Hungarian Revolution", "Berlin Wall", "Cuban Missile Crisis", "JFK Assassination", "SALT", "End of Vietnam War", "Fall of the Berlin Wall", "Reunification of Germany", "End of the Soviet Union"]

str_dates = ["1945-08-14", "1947-03-12", "1947-06-05", "1948-06-24", "1949-04-04", "1950-06-25", "1953-03-05", "1953-07-27", "1955-05-14", "1956-10-23", "1961-08-13", "1962-10-14", "1963-11-22", "1972-05-26", "1975-04-30", "1989-11-09", "1990-10-03", "1991-12-26"]
dates = [datetime.strptime(date, "%Y-%m-%d") for date in str_dates]

vline_heights = np.tile([-4, 4, -3, 3, -2, 2], (len(dates)//6 + 1))[:len(dates)]

fig, ax = plt.subplots(figsize=(10, 5))
ax.set(title="Cold War Timeline")

ax.plot(dates, np.zeros_like(dates), "-o", color="k", markerfacecolor="w")

for date, height, event in zip(dates, vline_heights, events):
    if height <= 0:
        vertical_alignment = "top"
    else:
        vertical_alignment = "bottom"
        
    ax.annotate(event, xy=(date, 0), xytext=(-3, np.sign(height)*3), textcoords="offset points", horizontalalignment="center", verticalalignment=vertical_alignment)

ax.xaxis.set_major_locator(mdates.YearLocator(10))
ax.xaxis.set_major_formatter(mdates.DateFormatter("%b %Y"))
plt.setp(ax.get_xticklabels(), rotation=30, ha="right")

ax.yaxis.set_visible(False)
ax.spines[["left", "top", "right"]].set_visible(False)

plt.show()
