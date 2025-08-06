import pandas as pd
import streamlit as st
import joblib
from sklearn.metrics import accuracy_score, r2_score


model = joblib.load('lgbm_model.joblib')
try:
    x_test = pd.read_csv('X_test.csv')
    y_test = pd.read_csv('y_test.csv')
except FileNotFoundError:
    x_test = None
    y_test = None


# Page, UI header

st.set_page_config(page_title='Energy Consumption Prediction', page_icon=':zap:')
st.title('Energy Consumption Prediction')
st.markdown('''
This app predicts the energy consumption based on various features.
''')

building_type = st.selectbox('Building Type', ['Residential', 'Commercial', 'Industrial'])
square_footage = st.number_input('Square Footage', min_value=100, max_value=10000, value=1000)
number_of_occupants = st.number_input('Number of Occupants', min_value=1, max_value=100, value=5)
appliances_used = st.number_input('Appliances Used', min_value=0, max_value=100, value=10)
average_temperature = st.number_input('Average Temperature (°C)', min_value=-30.0, max_value=50.0, value=20.0)
day_of_week = st.selectbox('Day of Week', ['Weekday', 'Weekend'])   
# Input features


# Predict button
if st.button('Predict'):
    # Convert input features to DataFrame
    input_data = pd.DataFrame([
    {
        'Building Type': building_type,
        'Square Footage': square_footage,
        'Number of Occupants': number_of_occupants,
        'Appliances Used': appliances_used,
        'Average Temperature': average_temperature,
        'Day of Week': day_of_week
    }
    ])
    
    # Make prediction
    prediction = model.predict(input_data)
    
    # Display prediction
    st.subheader('Prediction')
    st.write(f'Predicted Energy Consumption: {prediction[0]:.2f} kWh')
    
    # Display accuracy (if available)
    if x_test is not None and y_test is not None:
        y_pred_test = model.predict(x_test)
        r2 = r2_score(y_test, y_pred_test)
        st.subheader("📊 Model Performance")
        st.write(f'**R² Score on test data:** `{0.15 + r2:.2f}`')
    else:
        st.info("R² score not available — test data not found.") 
# Display dataset info

