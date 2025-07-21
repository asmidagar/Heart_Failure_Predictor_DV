from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)

# Load model and scaler from model.pkl
with open('model.pkl', 'rb') as f:
    model, scaler = pickle.load(f)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Read from inputs and convert to float
        features = [float(request.form[key]) for key in [
            'age', 'anaemia', 'diabetes', 'ejection_fraction',
            'high_blood_pressure', 'serum_sodium', 'sex',
            'smoking', 'time', 'log_cpk', 'log_platelets', 'log_serum_creatinine'
        ]]

        # Scale the input
        features_scaled = scaler.transform([features])

        # Make prediction
        prediction = model.predict(features_scaled)[0]
        result = "Patient is at risk of Heart Failure" if prediction == 1 else "Patient is not at risk"
    except Exception as e:
        result = f"Error: {str(e)}"

    return render_template('index.html', prediction_text=result)

if __name__ == '__main__':
    app.run(debug=True)