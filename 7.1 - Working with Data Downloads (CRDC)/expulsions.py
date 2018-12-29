## Explore expulsions by gender/race

if __name__ == "__main__":
    import pandas as pd
    import numpy as np
    data = pd.read_csv("data/CRDC2013_14.csv", encoding = "Latin-1")
    
    ## get rid of faulty data
    ## print(data["TOT_DISCWODIS_EXPZT_M"].value_counts())
    data = data.replace(value = 0, to_replace = -9)
    
    ## create categories interested
    races = ["HI", "AM", "AS", "HP", "BL", "WH", "TR"]
    genders = ["F", "M"]
    
    ## add a total_expulsion column, and compile all_expulsion
    data["total_expulsion"] = data["TOT_DISCWODIS_EXPZT_M"] + data["TOT_DISCWODIS_EXPZT_F"]
    all_expulsion = data["total_expulsion"].sum()

    ## create dictionary for totals to store distribution of each race
    totals = {}
    for race in races:
        race_f = "SCH_DISCWODIS_EXPZT_" + race + "_" + genders[0]
        race_m = "SCH_DISCWODIS_EXPZT_" + race + "_" + genders[1]
        total_race = "total_" + race 
        totals[total_race] = (data[race_m].sum() + data[race_f].sum()) / all_expulsion
        
    ## add genders for completion
    totals["TOT_DISCWODIS_EXPZT_M"] = data["TOT_DISCWODIS_EXPZT_M"].sum() / all_expulsion
    totals["TOT_DISCWODIS_EXPZT_F"] = data["TOT_DISCWODIS_EXPZT_F"].sum() / all_expulsion
    
    for k,v in totals.items():
        print (k, v)