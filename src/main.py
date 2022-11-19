import numpy as np
import pandas as pd
from scipy import sparse
from sklearn.preprocessing import normalize

interactions_df = pd.read_csv(
    "D:/Study/Python/RecomenationSystem/data/lastfm_user_scrobbles.csv")
titles_df = pd.read_csv(
    "D:/Study/Python/RecomenationSystem/data/lastfm_artist_list.csv")

# show in
interactions_df.groupby("user_id").count().mean()

# artist_names
titles_df.index = titles_df["artist_id"]
title_dict = titles_df["artist_name"].to_dict()

# get matrix
rows, r_pos = np.unique(interactions_df.values[:, 0], return_inverse=True)
cols, c_pos = np.unique(interactions_df.values[:, 1], return_inverse=True)
interactions_sparse = sparse.csr_matrix(
    (interactions_df.values[:, 2], (r_pos, c_pos)))
interactions_sparse

# normalize and get matrix
Pui = normalize(interactions_sparse, norm="l2", axis=1)
sim = Pui.T * Pui
interactions_sparse_transposed = interactions_sparse.transpose(copy=True)
Piu = normalize(interactions_sparse_transposed, norm='l2', axis=1)
fit = Pui * Piu * Pui

# start with 520
init_set = set([title_dict[i+1]
               for i in np.nonzero(interactions_sparse[520])[1].tolist()])

# user recomendations
pred_set = set([title_dict[i+1]
               for i in fit[520].toarray().argsort()[0][-70:].tolist()])
