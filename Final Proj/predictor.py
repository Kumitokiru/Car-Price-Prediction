import joblib
import logging

# Set up logging
logging.basicConfig(level=logging.DEBUG)

def predict_price(features):
    logging.debug(f"Features for prediction: {features}")
    try:
        model = joblib.load('models/model.pkl')  # Ensure this path is correct
        prediction = model.predict([features])[0]
        logging.debug(f"Prediction: {prediction}")
        return prediction
    except Exception as e:
        logging.error(f"Prediction failed with error: {e}")
        raise