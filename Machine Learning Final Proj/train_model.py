import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score
import pickle

# Load your dataset
data = pd.read_csv('data.csv')

# Print column names to inspect them
print("Columns in the dataset:", data.columns)

# One-hot encode the 'Make' column (car brand) to convert it to numerical format
data_encoded = pd.get_dummies(data, columns=['Make'], drop_first=True)

# Define the features and target
X = data_encoded[['Year', 'Engine HP', 'highway MPG'] + [col for col in data_encoded.columns if 'Make_' in col]]  # Include encoded 'Make' columns
y = data['MSRP']  # Target column (Price)

# Split the data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the model
model = RandomForestRegressor()
model.fit(X_train, y_train)

# Evaluate the model
y_pred = model.predict(X_test)
print("Mean Squared Error:", mean_squared_error(y_test, y_pred))
print("R² Score:", r2_score(y_test, y_pred))

# Save the model
with open('model.pkl', 'wb') as file:
    pickle.dump(model, file)

print("Model training complete. The model is saved as 'model.pkl'.")
