
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

st.title("Time Fractinal Black Scholes Partial Differential Equation")
if st.button("**Summary**"):
  st.subheader("**AI plus Partial Differential Eqns ie Physics Informed Neural Network (PINN) demonstration.**")
  st.write("**We'll explore implementing a PINN to optimize the efficiency and application of the Black Scholes Formula.**")
with st.sidebar:
  st.header("**Caputo Integer-Valued Derivatives**")
  st.write("May need to convert to integer value representations of fraction values.")
  st.slider("***d/dx***", min_value=0.0, max_value=1.0, step=0.125, format='%1.f')



