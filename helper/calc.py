import pandas as pd
import numpy as np
import json 
import seaborn as sns
import os
import re


def rango_percentilar(mydata, col_name, idx):
    "calcula el rengo percentilar de un valor de la columna"
    return np.mean(mydata[f"{col_name}"].to_numpy() <= mydata[f"{col_name}"].iloc[idx])


def to_percentile(mydata, col_name):
    "calcula el precentil de toda una columna"
    mydata = mydata.copy()
    mydata = mydata.reset_index()
    percentiles = [ ]
    for idx, series in mydata.iterrows():
        res = rango_percentilar(mydata, col_name, idx)
        percentiles.append(res)
    mydata[f"{col_name}_percentile"] = percentiles
    return mydata