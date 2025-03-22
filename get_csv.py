import pandas as pd

df = pd.read_csv("../csv/23456_big_artist_collab.csv")

smallDF = df[['item name','inscription text']].copy()

smallDF.to_csv("item_inscription.csv", index=False)