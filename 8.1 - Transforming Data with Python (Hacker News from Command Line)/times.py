# Find when the most articles are submitted
## edit: added code to account for different time measurements

import read
import pandas as pd
import dateutil as dt
#import datetime

def years(timestamp):
    time = dt.parser.parse(timestamp)
    return time.year

def months(timestamp):
    time = dt.parser.parse(timestamp)
    return time.month

def days(timestamp):
    time = dt.parser.parse(timestamp)
    return time.day

def hours(timestamp):
    time = dt.parser.parse(timestamp)
    return time.hour

def minutes(timestamp):
    time = dt.parser.parse(timestamp)
    return time.minute

hn = read.load_data()

hn["year"] = hn["submission_time"].apply(func = years)
print(hn["year"].value_counts())

hn["month"] = hn["submission_time"].apply(func = months)
print(hn["month"].value_counts())

hn["day"] = hn["submission_time"].apply(func = days)
print(hn["day"].value_counts())

hn["hour"] = hn["submission_time"].apply(func = hours)
print(hn["hour"].value_counts())

hn["minute"] = hn["submission_time"].apply(func = minutes)
print(hn["minute"].value_counts())
