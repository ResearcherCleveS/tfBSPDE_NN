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

st.header("Time Fractinal Black Scholes Partial Differential Equation")
if st.button("**Summary**"):
  st.title("**AI plus Partial Differential Eqns ie Physics Informed Neural Network (PINN) demonstration.**")
  st.caption("**We'll explore implementing a PINN to optimize the efficiency and application of the Black Scholes Formula.**")
