from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPRegressor
from sklearn.metrics import mean_absolute_error
import pandas as pd

# Read the data
df = pd.read_csv('weather.csv')

# Drop unnecessary columns
df.drop(columns=['Formatted Date', 'Daily Summary'], axis=1, inplace=True)

# Drop rows with missing values
df.dropna(inplace=True)

# Model 1: Predict Summary
df_1 = pd.get_dummies(df, columns=['Precip Type'])

# Standardize features
scaler = StandardScaler()
X_scaled_1 = scaler.fit_transform(df_1.drop(columns=['Summary']))
y_1 = df_1['Summary']

# Apply PCA
pca_1 = PCA(n_components=0.9)
X_pca_1 = pca_1.fit_transform(X_scaled_1)

# Split data
X_train_1, X_test_1, y_train_1, y_test_1 = train_test_split(X_pca_1, y_1, test_size=0.2, random_state=42)

# Initialize and train model_1
model_1 = MLPRegressor(hidden_layer_sizes=(64, 64), activation='relu', solver='adam', max_iter=200, random_state=42)
model_1.fit(X_train_1, y_train_1)

# Predict and evaluate
y_pred_1 = model_1.predict(X_test_1)
mae_1 = mean_absolute_error(y_test_1, y_pred_1)
print("Model 1 MAE:", mae_1)

# Model 2: Predict Temperature
df_2 = pd.get_dummies(df, columns=['Precip Type', 'Summary'])

# Standardize features
X_scaled_2 = scaler.fit_transform(df_2.drop(columns=['Temperature (C)']))
y_2 = df_2['Temperature (C)']

# Apply PCA
pca_2 = PCA(n_components=0.9)
X_pca_2 = pca_2.fit_transform(X_scaled_2)

# Split data
X_train_2, X_test_2, y_train_2, y_test_2 = train_test_split(X_pca_2, y_2, test_size=0.2, random_state=42)

# Initialize and train model_2
model_2 = MLPRegressor(hidden_layer_sizes=(64, 64), activation='relu', solver='adam', max_iter=200, random_state=42)
model_2.fit(X_train_2, y_train_2)

# Predict and evaluate
y_pred_2 = model_2.predict(X_test_2)
mae_2 = mean_absolute_error(y_test_2, y_pred_2)
print("Model 2 MAE:", mae_2)