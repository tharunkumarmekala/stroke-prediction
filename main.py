from flask import Flask, request, jsonify
import pandas as pd
import numpy as np
import joblib  # For loading the trained model

app = Flask(__name__)

# Load trained model
model = joblib.load("stroke_model.pkl")

# Define features expected from user input
expected_features = ['Age', 'BMI', 'FBS', 'Cholesterol', 'Hypertension', 'AFib']

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.json  # Get input as JSON
        features = np.array([data[feature] for feature in expected_features]).reshape(1, -1)

        prediction = model.predict(features)[0]
        confidence = model.predict_proba(features)[0][prediction]

        return jsonify({
            "stroke_risk": "Yes" if prediction == 1 else "No",
            "confidence": round(confidence * 100, 2)
        })

    except KeyError as e:
        return jsonify({"error": f"Missing input: {str(e)}"}), 400

if __name__ == '__main__':
    app.run(debug=True)
