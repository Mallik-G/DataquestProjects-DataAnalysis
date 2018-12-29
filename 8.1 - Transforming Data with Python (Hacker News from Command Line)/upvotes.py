# correlate total upvotes to time

import read
import pandas as pd
import dateutil as dt
import matplotlib.pyplot as plt

def years(timestamp):
    time = dt.parser.parse(timestamp)
    return time.year

def months(timestamp):
    time = dt.parser.parse(timestamp)
    return time.month

def hours(timestamp):
    time = dt.parser.parse(timestamp)
    return time.hour

hn = read.load_data()

hn["year"] = hn["submission_time"].apply(func = years)
years = [2007,2008,2009,2010,2011,2012,2013,2014,2015]

hn["month"] = hn["submission_time"].apply(func = months)
months = [1,2,3,4,5,6,7,8,9,10,11,12]

hn["hour"] = hn["submission_time"].apply(func = hours)
hours = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,1,20,21,22,23]

year_upvotes = {}
month_upvotes = {}
hour_upvotes = {}

for year in years:
    year_upvotes[year] = 0
    for row in range(len(hn)):
        if hn.iloc[row]["year"] == year:
            year_upvotes[year] += hn.iloc[row][1]

for month in months:
    month_upvotes[month] = 0
    for row in range(len(hn)):
        if hn.iloc[row]["month"] == month:
            month_upvotes[month] += hn.iloc[row][1]
            
for hour in hours:
    hour_upvotes[hour] = 0
    for row in range(len(hn)):
        if hn.iloc[row]["hour"] == hour:
            hour_upvotes[hour] += hn.iloc[row][1]

print("YEAR_UPVOTES\n")
print(year_upvotes)
a,b = (list(year_upvotes.keys()), list(year_upvotes.values()))
plt.plot(a,b)
plt.show()

print("\nMONTH_UPVOTES\n")
print(month_upvotes)
c,d = (list(month_upvotes.keys()), list(month_upvotes.values()))
plt.plot(c,d)
plt.show()

print("\nHOUR_UPVOTES\n")
print(hour_upvotes)
e,f = (list(hour_upvotes.keys()), list(hour_upvotes.values()))
plt.plot(e,f)
plt.show()
