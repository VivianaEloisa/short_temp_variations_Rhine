"""
Author: Viviana Eloisa Quezada Dominguez
The "config.py" file, is importing all the libraries and modules that are
required for the correct functionality of this code.

Also, in case one of the libraries or modules is not properly installed.
The user will be able to realize that is an ImportError with its respective
message.
"""

try:
    import os
    import logging
    import math
except ImportError:
    logging.info("ERROR: Cannot import basic Python libraries.")

try:
    import numpy as np
    import pandas as pd
    from scipy import stats
except ImportError:
    logging.info("ERROR: Cannot import SciPy libraries.")

try:
    import matplotlib.pyplot as plt
except ImportError:
    logging.info("ERROR: Cannot import Matplotlib libraries")

try:
    import tkinter as tk
    from tkinter.messagebox import showinfo
    from tkinter import ttk
except ImportError:
    logging.info("ERROR: Cannot import tkinter modules")

try:
    from openpyxl import load_workbook
except ImportError:
    logging.info("ERROR: Cannot import openpyxl libraries")

try:
    from sklearn.linear_model import LinearRegression
    from sklearn.preprocessing import scale
    from sklearn.preprocessing import StandardScaler
    from sklearn import decomposition
    from sklearn.model_selection import train_test_split
    from sklearn.metrics import r2_score

except ImportError:
    logging.info("ERROR: Cannot import Scikit learn libraries")

try:
    import plotly.express as px
    import plotly.graph_objects as go
except ImportError:
    logging.info("ERROR: Cannot import Plotly libraries")

try:
    plots_path = "C:/Users/Lenovo/Downloads/temp_var/results_thesis/plots"

except ImportError:
    logging.info("ERROR: Cannot find the plots path for saving the generated"
                 "plots.")

try:
    df_path = "C:/Users/Lenovo/Downloads/temp_var/results_thesis/df"

except ImportError:
    logging.info("ERROR: Cannot find the data frame path for saving the "
                 "generated data frames.")

# Creating the log file.
# logging.basicConfig(filename="my-logfile.log",
#                     format="%(asctime)s - %(message)s",
#                     filemode="w", level=logging.DEBUG)
