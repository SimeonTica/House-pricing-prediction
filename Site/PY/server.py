from flask import Flask, render_template, request, jsonify
from predictor import predict_price  # Import your prediction function

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Get data from the request
    data = request.get_json()

    # Extract features from the data
    area = float(data['area'])
    bedrooms = int(data['bedrooms'])
    bathrooms = int(data['bathrooms'])

    # Call your machine learning model
    predicted_price = predict_price(area, bedrooms, bathrooms)

    # Return the prediction as JSON
    return jsonify({'predicted_price': predicted_price})

if __name__ == '__main__':
    app.run(debug=True)
