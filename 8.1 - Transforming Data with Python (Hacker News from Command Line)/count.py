# count which words appear most often in headlines

import read
from collections import Counter

hn = read.load_data()
hn_headline = hn["headline"]

string = ""
for s in hn_headline:
    string += str(s) + ' '
    
print(Counter(string.lower().split()).most_common(100))
