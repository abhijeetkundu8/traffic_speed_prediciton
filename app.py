import streamlit as st
import pandas as pd
import joblib

# Load model
model = joblib.load('traffic_speed_model.pkl')

st.title("Traffic Speed Prediction App")

# Input fields
road_id = st.number_input("Road ID", min_value=1, max_value=300, value=5)
hour = st.slider("Hour of Day (0-23)", 0, 23, 14)
day_of_week = st.selectbox("Day of Week (0=Mon, 6=Sun)", [0,1,2,3,4,5,6])
lag1 = st.number_input("Speed (10 min ago)", value=45)
lag2 = st.number_input("Speed (20 min ago)", value=47)
lag3 = st.number_input("Speed (30 min ago)", value=50)

if st.button("Predict Speed"):
    new_input = pd.DataFrame([[road_id, hour, day_of_week, lag1, lag2, lag3]],
                             columns=['road_id','hour','day_of_week','lag1','lag2','lag3'])
    prediction = model.predict(new_input)[0]
    st.success(f"Predicted Speed: {prediction:.2f} km/h")
