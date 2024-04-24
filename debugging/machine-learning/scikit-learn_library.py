from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.model_selection import train_test_split
# from sklearn.ensemble import RandomForestClassifier
from sklearn.neural_network import MLPRegressor
from sklearn.metrics import accuracy_score
# from sklearn.metrics import accuracy_score, mean_squared_error
import pandas as pd

df = pd.read_csv('data/weather.csv')
df.drop(columns=['Formatted Date', 'Daily Summary'], axis=1, inplace=True)
df.dropna(inplace=True)

df_1 = pd.get_dummies(df, columns=['Precip Type'])

scaler = StandardScaler()
X_scaled_1 = scaler.fit_transform()
# X_scaled_1 = scaler.fit_transform(df_1.drop(columns=['Summary']))

pca = PCA(n_components=0.9)
X_pca_1 = pca.fit_transform(X_scaled_1)

X_train_1, X_test_1, y_train_1, y_test_1 = train_test_split(X_pca_1, df_1['Summary'], test_size=0.2, random_state=42)

# model_1 = RandomForestClassifier(n_estimators=100, random_state=42)
model_1.fit(X_train_1, y_train_1)
y_pred_1 = model_1.predict(X_test_1)

print("Model 1 accuracy:", accuracy_score(y_test_1, y_pred_1))

df_2 = pd.get_dummies(df, columns=['Precip Type', 'Summary'])

X_scaled_2 = scaler.fit_transform()
# X_scaled_2 = scaler.fit_transform(df_2.drop(columns=['Temperature (C)']))

X_pca_2 = pca.fit_transform(X_scaled_2)

X_train_2, X_test_2, y_train_2, y_test_2 = train_test_split(X_pca_2, df_2['Temperature (C)'], test_size=0.2, random_state=42)

model_2 = MLPRegressor(hidden_layer_sizes=(64, 64), activation='relu', solver='adam', max_iter=200, random_state=42)
model_2.fit(X_train_2, y_train_2)
y_pred_2 = model_2.predict(X_test_2)

print("Model 2 accuracy: ", accuracy_score(y_test_2, y_pred_2))
# print("Model 2 mean squared error: ", mean_squared_error(y_test_2, y_pred_2))