import numpy as np
import pandas as pd
from scipy import sparse
from sklearn.preprocessing import normalize

interactions_df = pd.read_csv(
    "D:/Study/Python/RecomenationSystem/data/lastfm_user_scrobbles.csv")
titles_df = pd.read_csv(
    "D:/Study/Python/RecomenationSystem/data/lastfm_artist_list.csv")
interactions_df
