# correlate submission time to upvotes

import read
import pandas as pd
import dateutil as dt

def months(timestamp):
    time = dt.parser.parse(timestamp)
    return time.month

def hours(timestamp):
    time = dt.parser.parse(timestamp)
    return time.hour

hn = read.load_data()

hn["month"] = hn["submission_time"].apply(func = months)
months = hn["month"].unique()

hn["hour"] = hn["submission_time"].apply(func = hours)
hours = hn["hour"].unique()

month_upvotes = {}
hour_upvotes = {}

for month in months:
    counter = 0
    month_upvotes[month] = 0
    for row in range(len(hn)):
        if hn.iloc[row]["month"] == month:
            month_upvotes[month] += hn.iloc[row][1]
            counter+= 1
    month_upvotes[month] = month_upvotes[month] / counter   
            
for hour in hours:
    counter = 0
    hour_upvotes[hour] = 0
    for row in range(len(hn)):
        if hn.iloc[row]["hour"] == hour:
            hour_upvotes[hour] += hn.iloc[row][1]
            counter+= 1
    hour_upvotes[hour] = hour_upvotes[hour] / counter   
            
sorted_month_upvotes = sorted(month_upvotes.items(), key = lambda value: value[1])
sorted_hour_upvotes = sorted(hour_upvotes.items(), key = lambda value: value[1])

print("MONTH_UPVOTES\n")
print(sorted_month_upvotes)
print("\nHOUR_UPVOTES\n")
print(sorted_hour_upvotes)
