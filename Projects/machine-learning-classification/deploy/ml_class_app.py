import streamlit as st
import pickle
import pandas as pd
import urllib.request
import xgboost as xgb


# Define the URL of the pickle model
model_url = 'https://github.com/rahul-bhutekar/Data-Science/raw/72b8eb0032d54f581957f4ff8bd4d8c21cf0d150/Projects/machine-learning-classification/deploy/classy_cc_transaction_fraud_detection.pkl'

# Download the model file
model_filename = 'classy_cc_transaction_fraud_detection.pkl'
urllib.request.urlretrieve(model_url, model_filename)


# Function to create a Bootstrap-like alert box
def bootstrap_alert(alert_type, message):
    alert_html = f"""
    <div style="padding: 15px; margin-bottom: 15px; border: 6px solid transparent; border-radius: 4px;
                background-color: {alert_type['bg_color']}; border-color: {alert_type['border_color']}; color: {alert_type['text_color']};">
        {message}
    </div>
    """
    st.markdown(alert_html, unsafe_allow_html=True)

# Define different alert types
alert_types = {
    "success": {"bg_color": "#d4edda", "border_color": "#c3e6cb", "text_color": "#155724"},
    "info": {"bg_color": "#d1ecf1", "border_color": "#bee5eb", "text_color": "#0c5460"},
    "warning": {"bg_color": "#fff3cd", "border_color": "#ffeeba", "text_color": "#f20808fa"},
    "danger": {"bg_color": "#f8d7da", "border_color": "#f5c6cb", "text_color": "#721c24"}
}

# Load the model from the file
with open(model_filename, 'rb') as model_file:
    ml_model = pickle.load(model_file)
    

# Define the Streamlit app
st.title("Credit Card Transaction Fraud Detection")
st.write("Enter transaction details to predict fraud or use sample inputs:")

# Sample inputs
fraud_samples = [
    "11,1004.95,148,-1,16114,42.005098,-80.485252,0.0176586",
    "8,875.38,148,-1,16114,40.917701,-80.014586,0.018423746",
    "4,283.65,148,-1,16114,41.122993,-79.556792,0.017508754",
    "2,15.49,765,-1,83869,47.978198,-117.265082,0.004664179",
    "11,821.89,148,-1,16114,40.7932,-80.433995,0.021653543"
]

non_fraud_samples = [
    "7,19.89,148,-1,16114,42.297246,-79.425116,0.003798155",
    "13,9.03,692,-1,41254,38.580916,-81.725325,0.004444444",
    "2,55.01,725,-1,78214,29.688173,-98.245038,0.005990783",
    "9,34.42,427,-1,56152,45.166439,-94.743248,0.001573564",
    "12,141.23,222,-1,31630,31.617466,-82.313895,0.00623053"
]

# Sidebar for sample inputs
st.sidebar.title("Sample Inputs")
st.sidebar.write("For fraudulent transactions, try these values:")

for i, sample in enumerate(fraud_samples):
    if st.sidebar.button(f'Fraud Sample {i+1}'):
        st.session_state.sample_input = sample

st.sidebar.write("For non-fraudulent transactions, try these values:")

for i, sample in enumerate(non_fraud_samples):
    if st.sidebar.button(f'Non-Fraud Sample {i+1}'):
        st.session_state.sample_input = sample

# Retrieve or initialize sample input
sample_input = st.session_state.get('sample_input', fraud_samples[0])
inputs = [float(x) for x in sample_input.split(",")]


# Function to create a Bootstrap-like alert box
def bootstrap_alert(alert_type, message):
    alert_html = f"""
    <div style="padding: 15px; margin-bottom: 15px; border: 6px solid transparent; border-radius: 4px;
                background-color: {alert_type['bg_color']}; border-color: {alert_type['border_color']}; color: {alert_type['text_color']};">
        {message}
    </div>
    """
    st.markdown(alert_html, unsafe_allow_html=True)

# Define different alert types
alert_types = {
    "success": {"bg_color": "#d4edda", "border_color": "#c3e6cb", "text_color": "#155724"},
    "info": {"bg_color": "#d1ecf1", "border_color": "#bee5eb", "text_color": "#0c5460"},
    "warning": {"bg_color": "#fff3cd", "border_color": "#ffeeba", "text_color": "#f20808fa"},
    "danger": {"bg_color": "#f8d7da", "border_color": "#f5c6cb", "text_color": "#721c24"}
}

bootstrap_alert(alert_types["info"], "Please encode categorical data (e.g., category) and ensure numeric fields (e.g., amount) have valid values.")

# Collect user input
transaction_data = {}
transaction_data['category'] = st.number_input("Category:", value=inputs[0])
transaction_data['amt'] = st.number_input("Amount:", value=inputs[1])
transaction_data['city'] = st.number_input("City:", value=inputs[2])
transaction_data['state'] = st.number_input("State:", value=inputs[3])
transaction_data['zip'] = st.number_input("Zip:", value=inputs[4])
transaction_data['merch_lat'] = st.number_input("Merchant Latitude:", value=inputs[5])
transaction_data['merch_long'] = st.number_input("Merchant Longitude:", value=inputs[6])
transaction_data['merchant_mean_encoded'] = st.number_input("Merchant:", value=inputs[7])

# Convert input data to a DataFrame
input_df = pd.DataFrame([transaction_data])

# Make a prediction
if st.button("Predict"):
    prediction = ml_model.predict(input_df)
    if prediction[0] == 1:
        bootstrap_alert(alert_types["warning"], "The transaction is likely to be fraudulent based on the provided details.")
    else:
        bootstrap_alert(alert_types["info"], "The transaction does not appear to be fraudulent based on the provided details.")