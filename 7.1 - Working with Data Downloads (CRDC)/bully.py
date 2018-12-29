## Explore bullying by gender/race - basis of race, color, national origin

if __name__ == "__main__":
    import pandas as pd
    import numpy as np
    data = pd.read_csv("data/CRDC2013_14.csv", encoding = "Latin-1")
    
    ## get rid of faulty data
    ## print(data["TOT_HBREPORTED_RAC_M"].value_counts())
    ## print(data["TOT_HBDISCIPLINED_RAC_M"].value_counts())
    data = data.replace(value = 0, to_replace = -9)
    data = data.replace(value = 0, to_replace = -5)
    
    ## create categories interested
    races = ["HI", "AM", "AS", "HP", "BL", "WH", "TR"]
    genders = ["F", "M"]
    
    ## add a total_bully, total_bullied column, and compile all_bully, all_bullied
    data["total_bully"] = data["TOT_HBDISCIPLINED_RAC_M"] + data["TOT_HBDISCIPLINED_RAC_F"]
    all_bully = data["total_bully"].sum()
    
    data["total_bullied"] = data["TOT_HBREPORTED_RAC_M"] + data["TOT_HBREPORTED_RAC_F"]
    all_bullied = data["total_bullied"].sum()

    ## create dictionary for totals to store distribution of each race
    totals = {}
    for race in races:
        race_f_bully = "SCH_HBDISCIPLINED_RAC_" + race + "_" + genders[0]
        race_m_bully = "SCH_HBDISCIPLINED_RAC_" + race + "_" + genders[1]
        total_race = "total_" + race + "_bully"
        totals[total_race] = (data[race_m_bully].sum() + data[race_f_bully].sum()) / all_bully
        
        race_f_bullied = "SCH_HBREPORTED_RAC_" + race + "_" + genders[0]
        race_m_bullied = "SCH_HBREPORTED_RAC_" + race + "_" + genders[1]
        total_race = "total_" + race + "_bullied"
        totals[total_race] = (data[race_m_bullied].sum() + data[race_f_bullied].sum()) / all_bullied
        
    ## add genders for completion
    totals["TOT_HBDISCIPLINED_RAC_M"] = data["TOT_HBDISCIPLINED_RAC_M"].sum() / all_bully
    totals["TOT_HBDISCIPLINED_RAC_F"] = data["TOT_HBDISCIPLINED_RAC_F"].sum() / all_bully
    
    totals["TOT_HBREPORTED_RAC_M"] = data["TOT_HBREPORTED_RAC_M"].sum() / all_bullied
    totals["TOT_HBREPORTED_RAC_F"] = data["TOT_HBREPORTED_RAC_F"].sum() / all_bullied
    
    for k,v in totals.items():
        print (k, v)
        