## Explore preschool enrollment by gender/race

if __name__ == "__main__":
    import pandas as pd
    import numpy as np
    data = pd.read_csv("data/CRDC2013_14.csv", encoding = "Latin-1")
    
    ## get rid of faulty data
    ## print(data["TOT_PSENR_M"].value_counts())
    data = data.replace(value = 0, to_replace = -9)
    
    ## create categories interested
    races = ["HI", "AM", "AS", "HP", "BL", "WH", "TR"]
    genders = ["F", "M"]
    
    ## add a total_pre column, and compile all_pre
    data["total_pre"] = data["TOT_PSENR_M"] + data["TOT_PSENR_F"]
    all_pre = data["total_pre"].sum()

    ## create dictionary for totals to store distribution of each race
    totals = {}
    for race in races:
        race_f = "SCH_PSENR_" + race + "_" + genders[0]
        race_m = "SCH_PSENR_" + race + "_" + genders[1]
        total_race = "total_" + race 
        totals[total_race] = (data[race_m].sum() + data[race_f].sum()) / all_pre
        
    ## add genders for completion
    totals["TOT_PSENR_M"] = data["TOT_PSENR_M"].sum() / all_pre
    totals["TOT_PSENR_F"] = data["TOT_PSENR_F"].sum() / all_pre
    
    for k,v in totals.items():
        print (k, v)
        