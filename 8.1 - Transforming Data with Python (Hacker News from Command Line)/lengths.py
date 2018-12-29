# correlate headline lengths to upvotes

import read
import pandas as pd

def count_headlines(headline):
    if pd.isnull(headline):
        return 0
    else:
        headline = str(headline)
        length = len(headline)
        return length

hn = read.load_data()

hn["headline"] = hn["headline"].apply(func = count_headlines)
headline_lengths = hn["headline"].unique()

upvotes = {}

for l in headline_lengths:
    counter = 0
    upvotes[l] = 0
    for row in range(len(hn)):
        if hn.iloc[row][3] == l:
            upvotes[l] += hn.iloc[row][1]
            counter+= 1
    upvotes[l] = upvotes[l] / counter        
    
sorted_upvotes = sorted(upvotes.items(), key = lambda value: value[1])
print(sorted_upvotes)   
