## Explore magnet school distribution by gender/race

if __name__ == "__main__":
    import pandas as pd
    import numpy as np
    data = pd.read_csv("data/CRDC2013_14.csv", encoding = "Latin-1")
    
    ## get magnet information - binary column
    ## print(data["SCH_STATUS_MAGNET"].value_counts())
    
    ## create categories interested
    races = ["HI", "AM", "AS", "HP", "BL", "WH", "TR"]
    genders = ["F", "M"]
    
    ## create separate YES/NO dataframes
    magnet = data[data["SCH_STATUS_MAGNET"] == "YES"]
    no_magnet = data[data["SCH_STATUS_MAGNET"] == "NO"]
    
    ## add a total_magnet, and compile all_magnet for each 
    data["total_magnet"] = magnet["TOT_ENR_M"] + magnet["TOT_ENR_F"]
    all_magnet = data["total_magnet"].sum()
                     
    data["total_no_magnet"] = no_magnet["TOT_ENR_M"] + no_magnet["TOT_ENR_F"]
    all_no_magnet = data["total_no_magnet"].sum()

    ## create dictionary for totals to store distribution of each race
    totals = {}
    for race in races:
        race_f = "SCH_ENR_" + race + "_" + genders[0]
        race_m = "SCH_ENR_" + race + "_" + genders[1]
        total_race = "total_" + race + "_magnet"
        totals[total_race] = (magnet[race_m].sum() + magnet[race_f].sum()) / all_magnet

        total_race = "total_" + race + "_no_magnet"
        totals[total_race] = (no_magnet[race_m].sum() + no_magnet[race_f].sum()) / all_no_magnet
        
    ## add genders for completion
    totals["TOT_ENR_M_magnet"] = magnet["TOT_ENR_M"].sum() / all_magnet
    totals["TOT_ENR_F_magnet"] = magnet["TOT_ENR_F"].sum() / all_magnet
                     
    totals["TOT_ENR_M_no_magnet"] = no_magnet["TOT_ENR_M"].sum() / all_no_magnet
    totals["TOT_ENR_F_no_magnet"] = no_magnet["TOT_ENR_F"].sum() / all_no_magnet
    
    for k,v in totals.items():
        print (k, v)