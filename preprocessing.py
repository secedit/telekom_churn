import pandas as pd
from sklearn.preprocessing import MinMaxScaler

from collections import Counter
import numpy as np

def preprocess(df, option):
    """
    This function is to cover all the preprocessing steps on the churn dataframe. It involves selecting important features, encoding categorical data, handling missing values,feature scaling and splitting the data
    """

    from sklearn.preprocessing import StandardScaler
    sc = StandardScaler()
    df2 = sc.fit_transform(df2)


    return df2
