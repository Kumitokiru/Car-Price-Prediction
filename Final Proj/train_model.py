import joblib
from sklearn.ensemble import RandomForestRegressor
from data_handler import load_data

# Load data
X_train, X_test, y_train, y_test = load_data('data.csv')

# Train model
model = RandomForestRegressor()
model.fit(X_train, y_train)

# Save model
joblib.dump(model, 'models/model.pkl')