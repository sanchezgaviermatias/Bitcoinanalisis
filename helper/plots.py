import pandas as pd
import numpy as np
import json 
import seaborn as sns
import os
import re
from pylab import mpl, plt

plt.style.use('seaborn')
mpl.rcParams['savefig.dpi'] = 300
mpl.rcParams['font.family'] = 'serif'


def plot_mayer(mydata, x="time", y="price", hue="Mayer_percentile"):
    f, ax = plt.subplots(figsize=(15, 11))
    sns.despine(f, left=True, bottom=True)
    sns.scatterplot(x, y,
                    hue=hue, 
                    sizes=(10, 20),
                    alpha=.5,
                    palette="rocket", 
                    data=mydata, ax=ax)

