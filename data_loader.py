import pandas as pd
import streamlit as st

@st.cache_data
def load_data(uploaded_file):
    """Load and preprocess data from uploaded file"""
    try:
        # Read the uploaded file
        if uploaded_file.name.endswith('.csv'):
            df = pd.read_csv(uploaded_file)
        else:
            # For other file types, we can add support later
            df = pd.read_csv(uploaded_file)
        
        # Check and clean data
        if 'Date' not in df.columns:
            st.error("CSV file must contain 'Date' column")
            return None
        
        # Remove any rows where Date is not a proper date
        df['Date'] = pd.to_datetime(df['Date'], errors='coerce')
        df = df.dropna(subset=['Date'])
        
        # Remove the NFLX header row if present
        df = df[~df['Date'].astype(str).str.contains('NFLX')]
        
        # Convert numeric columns
        numeric_cols = ['Open', 'High', 'Low', 'Close', 'Volume']
        for col in numeric_cols:
            if col in df.columns:
                df[col] = pd.to_numeric(df[col], errors='coerce')
        
        df.set_index('Date', inplace=True)
        df.sort_index(inplace=True)
        
        # Handle missing values
        df = df.fillna(method='ffill')
        
        # Calculate additional metrics
        df['Daily_Return'] = df['Close'].pct_change() * 100
        df['Cumulative_Return'] = (1 + df['Daily_Return']/100).cumprod() - 1
        
        return df
    except Exception as e:
        st.error(f"Error loading data: {str(e)}")
        return None