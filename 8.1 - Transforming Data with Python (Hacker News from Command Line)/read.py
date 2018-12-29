# read the data in 

import pandas as pd

def load_data():
    df = pd.read_csv("hn_stories.csv", sep = ',', names = ["submission_time", "upvotes", "url", "headline"])
    return df
