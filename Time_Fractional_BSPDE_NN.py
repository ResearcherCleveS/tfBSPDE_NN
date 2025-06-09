
import numpy as np
import streamlit as st
import yfinance as yf
import pandas as pd
import numpy as np
from datetime import timedelta
from scipy.stats import norm
from scipy.optimize import brentq
from scipy.interpolate import griddata
import plotly.graph_objects as go
#import pandas as pd
import matplotlib.pyplot as plt

st.title("Time Fractinal Black-Scholes Partial Differential Equation")

# with st.sidebar:
#   if st.button("**Summary**"):
#     st.subheader("**AI plus Partial Differential Eqns ie Physics Informed Neural Network (PINN) demonstration.**")
#     st.write("**We'll explore implementing a PINN to optimize the efficiency and application of the Black Scholes Formula.**")



if st.button("**Summary**"):
  st.subheader("**AI plus Partial Differential Eqns ie Physics Informed Neural Network (PINN) demonstration.**")
  st.write("**We'll explore implementing a PINN to optimize the efficiency and application of the Black Scholes Formula.**")

st.sidebar.header("**Caputo Integer-Valued Derivatives**")
st.sidebar.write("May need to convert to integer value representations of fraction values.")
st.sidebar.slider("𝗗𝛂", min_value=0.0, max_value=1.0, step=0.125, format='%.3f')

st.sidebar.header("**𝗗𝛂**")
𝗗𝛂 = st.sidebar.number_input(
    min_value=0.0,
    max_value=1.0,
    value=0.25,
    step=0.05,
    format="%.01f"
)

# with st.sidebar:
#   st.header("**Caputo Integer-Valued Derivatives**")
#   st.write("May need to convert to integer value representations of fraction values.")
#   # st.markdown("$\sf d\over{\sf dx}$")
#   st.slider("𝗗𝛂", min_value=0.0, max_value=1.0, step=0.125, format='%.3f')

# T = Maturity time of put option
# t = [0, T]
# S = stock price
# 𝑼(S, t) = the price of the option as a function of S and t.
# 𝞼 = the the volatility of the stock
# r = the risk-free interest rate
# The Caputo 
# 𝛂 = 2. I assume 𝛂-order derivative is 2, for 𝛂 ∈ [n-1, n], n ∈ ℕ, since the Black Scholes Eqn is second order.

st.sidebar.header('Strike Price Filter Parameters')

min_strike_pct = st.sidebar.number_input(
    'Minimum Strike Price (% of Spot Price)',
    min_value=50.0,
    max_value=199.0,
    value=80.0,
    step=1.0,
    format="%.1f"
)
