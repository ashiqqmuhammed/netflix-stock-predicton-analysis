import pandas as pd
import numpy as np

def calculate_performance_metrics(df):
    """Calculate comprehensive performance metrics"""
    metrics = {}
    
    # Price metrics
    metrics['Current_Price'] = df['Close'].iloc[-1]
    metrics['All_Time_High'] = df['Close'].max()
    metrics['All_Time_Low'] = df['Close'].min()
    metrics['52_Week_High'] = df['Close'].rolling(window=252).max().iloc[-1]
    metrics['52_Week_Low'] = df['Close'].rolling(window=252).min().iloc[-1]
    
    # Return metrics
    metrics['YTD_Return'] = df['Close'].pct_change(periods=len(df[df.index.year == df.index[-1].year])).iloc[-1] * 100
    metrics['Monthly_Return'] = df['Close'].pct_change(periods=21).iloc[-1] * 100
    metrics['Weekly_Return'] = df['Close'].pct_change(periods=5).iloc[-1] * 100
    metrics['Daily_Return'] = df['Daily_Return'].iloc[-1]
    
    # Risk metrics
    metrics['Volatility'] = df['Daily_Return'].std()
    metrics['Sharpe_Ratio'] = metrics['Daily_Return'] / metrics['Volatility'] if metrics['Volatility'] != 0 else 0
    metrics['Max_Drawdown'] = ((df['Close'] / df['Close'].cummax()) - 1).min() * 100
    
    # Volume metrics
    metrics['Avg_Daily_Volume'] = df['Volume'].mean()
    metrics['Current_Volume'] = df['Volume'].iloc[-1]
    metrics['Volume_Ratio'] = metrics['Current_Volume'] / metrics['Avg_Daily_Volume']
    
    return metrics