import numpy as np
import pandas as pd
from scipy import sparce
from sklearn.preprocessing import normalize

interactions_df = pd.read_csv("data/lastfm_user_scrobbles.csv")
titles_df = pd.read_csv("data/lastfm_artist_list.csv")

interactions_df
