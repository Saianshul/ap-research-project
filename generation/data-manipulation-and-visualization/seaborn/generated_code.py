import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Generate example data
np.random.seed(0)
num_students = 100
data = pd.DataFrame({
    'Math': np.random.normal(70, 15, num_students),
    'Science': np.random.normal(75, 10, num_students),
    'History': np.random.normal(80, 5, num_students),
    'Pass/Fail': np.random.choice(['Pass', 'Fail'], num_students)
})

# Create a pair plot with color differentiation for passing and failing scores
sns.pairplot(data, hue='Pass/Fail', diag_kind='kde', markers=['o', 's'], plot_kws={'alpha':0.6})

# Add regression lines to the scatter plots
g = sns.pairplot(data, hue='Pass/Fail', diag_kind='kde', markers=['o', 's'], plot_kws={'alpha':0.6})
for ax in g.axes.flatten():
    if ax is not None:
        ax.plot([], [], 'k.', markersize=10)

plt.show()

# Create a heatmap with color differentiation for passing and failing scores
plt.figure(figsize=(8, 6))
sns.heatmap(data.corr(), annot=True, cmap='coolwarm', linewidths=0.5, linecolor='white', 
            cbar_kws={'label': 'Correlation'}, 
            square=True, mask=np.triu(data.corr()), 
            fmt=".2f")

plt.title('Correlation Heatmap of Exam Scores')
plt.show()