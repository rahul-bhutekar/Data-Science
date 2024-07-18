from flask import Flask, render_template, request, session
import pickle
import numpy as np

app = Flask(__name__)

# Load the models and scalers
ml_model = pickle.load(open('log_reg_model.pkl', 'rb'))
ml_scaler_x = pickle.load(open('log_reg_scaler.pkl', 'rb'))
ml_scaler_y = pickle.load(open('log_reg_scaler_y.pkl', 'rb'))

@app.route('/clear_session')
def clear_session():
    session.clear()
    return 'Session cleared'

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Collect input data from the form
    
    inputs = [
        int(request.form['school']),
        int(request.form['age']),
        int(request.form['famsize']),
        int(request.form['Medu']),
        int(request.form['Fedu']),
        int(request.form['Mjob']),
        int(request.form['Fjob']),
        int(request.form['reason']),
        int(request.form['guardian']),
        int(request.form['traveltime']),
        int(request.form['studytime']),
        int(request.form['failures']),
        int(request.form['activities']),
        int(request.form['higher']),
        int(request.form['internet']),
        int(request.form['famrel']),
        int(request.form['freetime']),
        int(request.form['goout']),
        int(request.form['Dalc']),
        int(request.form['Walc']),
        int(request.form['health']),
        int(request.form['absences']),
        int(request.form['G1']),
        int(request.form['G2'])
    ]

    # Convert inputs to numpy array and apply scaling
    input_array = np.array(inputs).reshape(1, -1)
    scaled_inputs = ml_scaler_x.transform(input_array)

    # Predict the output using the model
    prediction = ml_model.predict(scaled_inputs)

    # Convert the prediction back to the original scale
    original_scale_prediction = ml_scaler_y.inverse_transform(prediction.reshape(-1, 1))

    # Prepare the output message
    prediction_text = f"The predicted grade of the student based on the provided values is {original_scale_prediction[0][0]:.2f}"

    return render_template('index.html', prediction_text=prediction_text)

if __name__ == "__main__":
    app.run(debug=True)
