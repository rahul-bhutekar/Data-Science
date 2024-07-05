import pickle
from flask import Flask, request, app, jsonify, render_template
import pandas as pd

app = Flask(__name__)

# load model
ml_model = pickle.load(open('classy_cc_transaction_fraud_detection.pkl', 'rb'))

# Define the expected feature names
expected_features = ['category', 'amt', 'city', 'state', 'zip', 'merch_lat', 'merch_long', 'merchant_mean_encoded']

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict_api', methods=['POST'])
def predict_api():
    try:
        # Get JSON data from the request
        json_data = request.get_json()

        # Extract 'data' from the JSON
        data = json_data.get('data')

        if data is None:
            return jsonify({"error": "Invalid input, no data found"}), 400
        
        # Convert data to DataFrame
        df = pd.DataFrame([data], columns=expected_features)

        output = ml_model.predict(df)
        # print(output[0])

        # Assuming the model returns a numpy array, convert it to a list
        prediction = output.tolist()

        # Return the prediction as JSON
        return jsonify({"prediction": prediction}), 200
        # return jsonify(prediction), 200
    
    except Exception as e:
        return jsonify({"error": str(e)}), 400
    
@app.route('/predict',methods=['POST'])
def predict():
    try:
        data=[float(x) for x in request.form.values()]

        if data is None:
            return jsonify({"error": "Invalid input, no data found"}), 400
        
        # Convert data to DataFrame
        df = pd.DataFrame([data], columns=expected_features)

        output = ml_model.predict(df)
        # return jsonify(prediction)

        # Return the prediction as Output Tesult
        if output == 1:
            return render_template("index.html",prediction_text="<div class=\"alert alert-danger\" role=\"alert\">The transaction is likely to be fraudulent based on the provided details.</div>")
        else:
            return render_template("index.html",prediction_text="<div class=\"alert alert-success\" role=\"alert\">The transaction does not appear to be fraudulent based on the provided details.</div>")
        
    except Exception as e:
        return jsonify({"error": str(e)}), 400
    

if __name__ == "__main__":
    app.run(debug=True)