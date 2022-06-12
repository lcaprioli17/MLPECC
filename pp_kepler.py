import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


def pre_process():
    kepler = pd.read_csv('./dataset/Kepler Objects of Interests.csv', on_bad_lines='skip')
    thresh = len(kepler) * .7
    kepler.dropna(thresh=thresh, axis=1, inplace=True)
    print(kepler['koi_disposition'].unique())
    print(kepler.columns.size)


