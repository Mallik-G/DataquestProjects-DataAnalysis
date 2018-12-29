# explore which domains were sumitted most often 
## edit: added code to account for subdomains

import read
import pandas as pd

def remove_subdomain(url):
    if pd.isnull(url):
        return url
    url = str(url)
    if url.count('.') > 1:
        index = url.find('.')
        sub_url = url[index+1:]
        return sub_url
    else:
        return url

hn = read.load_data()

domains = hn["url"].apply(func = remove_subdomain).value_counts()
domains = domains[:99:]
for name, row in domains.items():
    print("{0}: {1}".format(name,row))
    