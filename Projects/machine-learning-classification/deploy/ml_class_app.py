import streamlit as st
import pickle
import pandas as pd

# Load the model from the file
with open('https://github.com/rahul-bhutekar/Data-Science/blob/72b8eb0032d54f581957f4ff8bd4d8c21cf0d150/Projects/machine-learning-classification/deploy/classy_cc_transaction_fraud_detection.pkl', 'rb') as model_file:
    ml_model = pickle.load(model_file)

# Define the Streamlit app
st.title("Credit Card Transaction Fraud Detection")

# Collect user input
transaction_data = {}
transaction_data['category'] = st.number_input("Category:")
transaction_data['amt'] = st.number_input("Amount:")
transaction_data['city'] = st.number_input("City:")
transaction_data['state'] = st.number_input("State:")
transaction_data['zip'] = st.number_input("Zip:")
transaction_data['merch_lat'] = st.number_input("Merchant Latitude:")
transaction_data['merch_long'] = st.number_input("Merchant Longitude:")
transaction_data['merchant_mean_encoded'] = st.number_input("Merchant:")

# Convert input data to a DataFrame
input_df = pd.DataFrame([transaction_data])

# Make a prediction
if st.button("Predict"):
    prediction = ml_model.predict(input_df)
    st.write(f"Prediction: {'Fraud' if prediction[0] == 1 else 'Not Fraud'}")