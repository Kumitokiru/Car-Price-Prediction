from flask import Flask, request, render_template
from predictor import predict_price  # Import here at the top

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.form
    
    # Mapping categorical data
    engine_type_mapping = {'petrol': 0, 'diesel': 1}
    brand_mapping = {'brandA': 0, 'brandB': 1}  # Adjust based on your data
    
    # Ensure all required fields are present
    if 'mileage' not in data or 'brand' not in data or 'engine_type' not in data or 'age' not in data:
        return "Missing input data", 400  # Return an error response with status code 400
    
    # Input validation for mileage and age
    try:
        features = [
            float(data['mileage']),
            brand_mapping[data['brand']],  # Encode brand
            engine_type_mapping[data['engine_type']],  # Encode engine type
            int(data['age'])
        ]
    except ValueError as e:
        return f"Invalid input, please enter valid numbers for mileage and age. Error: {str(e)}", 400
    
    # Log the features for debugging
    print(f"Features for prediction: {features}")
    
    try:
        # Call the function from predictor.py
        price = predict_price(features)
    except Exception as e:
        # Log the error if model prediction fails
        return f"Prediction failed with error: {str(e)}", 500
    
    return render_template('result.html', price=round(price, 2))

if __name__ == '__main__':
    app.run(debug=True)