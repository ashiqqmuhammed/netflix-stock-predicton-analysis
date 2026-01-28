import streamlit as st
import pandas as pd
import numpy as np
from datetime import timedelta
from statsmodels.tsa.statespace.sarimax import SARIMAX

def train_sarima_model(df, forecast_days=365):
    """Train SARIMA model for forecasting"""
    try:
        # Use the last 3 years of data for training
        train_end_date = df.index[-1] - pd.DateOffset(years=3)
        train_data = df.loc[train_end_date:, 'Close']
        
        # Fit SARIMA model with auto-tuning
        # You can adjust these parameters based on your data
        order = (1, 1, 1)  # (p, d, q)
        seasonal_order = (1, 1, 1, 12)  # (P, D, Q, s) - monthly seasonality
        
        model = SARIMAX(train_data,
                       order=order,
                       seasonal_order=seasonal_order,
                       enforce_stationarity=False,
                       enforce_invertibility=False)
        
        model_fit = model.fit(disp=False)
        
        # Make predictions
        forecast = model_fit.forecast(steps=forecast_days)
        
        # Create future dates
        last_date = df.index[-1]
        future_dates = [last_date + timedelta(days=i) for i in range(1, forecast_days + 1)]
        
        # Calculate confidence intervals
        forecast_ci = model_fit.get_forecast(steps=forecast_days).conf_int()
        
        return {
            'forecast': forecast,
            'future_dates': future_dates,
            'model': model_fit,
            'confidence_intervals': forecast_ci,
            'order': order,
            'seasonal_order': seasonal_order
        }
        
    except Exception as e:
        st.error(f"Error in SARIMA model training: {str(e)}")
        return None