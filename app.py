import streamlit as st
import pandas as pd
import joblib

st.title("Retail Demand Forecast")

model = joblib.load('models/demand_forecast_model.pkl')

price = st.number_input("Enter product price")
promotion = st.selectbox("Promotion?", ["Yes", "No"]) == "Yes"
holiday = st.selectbox("Holiday?", ["Yes", "No"]) == "Yes"
day = st.slider("Day of Week", 0, 6)
month = st.slider("Month", 1, 12)

input_df = pd.DataFrame({
    'Price': [price],
    'Is_Promotion': [int(promotion)],
    'Is_Holiday': [int(holiday)],
    'DayOfWeek': [day],
    'Month': [month]
})

if st.button("Predict Demand"):
    prediction = model.predict(input_df)
    st.success(f"Predicted Units Sold: {int(prediction[0])}")
