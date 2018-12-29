## Explore enrollments by gender/race

if __name__ == "__main__":
    import pandas as pd
    ## add numpy
    import numpy as np
    data = pd.read_csv("data/CRDC2013_14.csv", encoding = "Latin-1")
    
    ## create categories interested
    races = ["HI", "AM", "AS", "HP", "BL", "WH", "TR"]
    genders = ["F", "M"]
    
    ## add a total_enrollment column, and compile all_enrollment
    data["total_enrollment"] = data["TOT_ENR_M"] + data["TOT_ENR_F"]
    all_enrollment = data["total_enrollment"].sum()

    ## create dictionary for totals to store distribution of each race
    totals = {}
    for race in races:
        race_f = "SCH_ENR_" + race + "_" + genders[0]
        race_m = "SCH_ENR_" + race + "_" + genders[1]
        total_race = "total_" + race 
        totals[total_race] = (data[race_m].sum() + data[race_f].sum()) / all_enrollment
        
    ## add genders for completion
    totals["TOT_ENR_M"] = data["TOT_ENR_M"].sum() / all_enrollment
    totals["TOT_ENR_F"] = data["TOT_ENR_F"].sum() / all_enrollment
    
    for k,v in totals.items():
        print (k, v)
        