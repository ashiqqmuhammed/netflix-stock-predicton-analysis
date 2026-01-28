# import streamlit as st
# import pickle
# import numpy as np

# # Load model
# with open("C:\Users\ashiq\OneDrive\Desktop\new\netflix_api\netflix_stock_data_yfinance.csv", "rb") as f:
#     model = pickle.load(f)

# # App title
# st.title("Netflix Stock Price Prediction")
# st.write("Predict the closing price using ML model")

# # Input fields
# open_price = st.number_input("Open Price", min_value=0.0)
# high_price = st.number_input("High Price", min_value=0.0)
# low_price = st.number_input("Low Price", min_value=0.0)
# volume = st.number_input("Volume", min_value=0.0)

# # Predict button
# if st.button("Predict Closing Price"):
#     input_data = np.array([[open_price, high_price, low_price, volume]])
#     prediction = model.predict(input_data)

#     st.success(f"Predicted Closing Price: {prediction[0]:.2f}")


import streamlit as st
import pickle
import numpy as np

# Load trained model (PKL FILE)
model_path = r"C:/Users/ashiq/OneDrive/Desktop/new/netflix_api/main.py"

with open(model_path, "rb") as f:
    model = pickle.load(f)

# App title
st.title("Netflix Stock Price Prediction")
st.write("Predict the closing price using ML model")

# Input fields
open_price = st.number_input("Open Price", min_value=0.0)
high_price = st.number_input("High Price", min_value=0.0)
low_price = st.number_input("Low Price", min_value=0.0)
volume = st.number_input("Volume", min_value=0.0)

# Predict button
if st.button("Predict Closing Price"):
    input_data = np.array([[open_price, high_price, low_price, volume]])
    prediction = model.predict(input_data)

    st.success(f"Predicted Closing Price: {prediction[0]:.2f}")
