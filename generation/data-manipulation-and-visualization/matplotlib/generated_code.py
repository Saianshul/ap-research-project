import matplotlib.pyplot as plt
from matplotlib.widgets import Cursor
import numpy as np

# Generate some random data
np.random.seed(0)
x = np.random.randn(100)
y = np.random.randn(100)

fig, ax = plt.subplots()
ax.scatter(x, y)
ax.set_title('Interactive Scatter Plot')
ax.set_xlabel('X')
ax.set_ylabel('Y')

# Create an annotation object
annot = ax.annotate("", xy=(0,0), xytext=(-20,20), textcoords="offset points",
                    bbox=dict(boxstyle="round", fc="w"),
                    arrowprops=dict(arrowstyle="->"))

# Make the annotation visible on hover
annot.set_visible(False)

def update_annot(ind):
    pos = sc.get_offsets()[ind["ind"][0]]
    annot.xy = pos
    text = f'({pos[0]:.2f}, {pos[1]:.2f})'
    annot.set_text(text)

def hover(event):
    vis = annot.get_visible()
    if event.inaxes == ax:
        cont, ind = sc.contains(event)
        if cont:
            update_annot(ind)
            annot.set_visible(True)
            fig.canvas.draw_idle()
        else:
            if vis:
                annot.set_visible(False)
                fig.canvas.draw_idle()

# Connect the hover function to the event
fig.canvas.mpl_connect("motion_notify_event", hover)

plt.show()