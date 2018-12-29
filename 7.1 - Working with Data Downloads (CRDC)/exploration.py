##Explore JJ an SCH_STATUS_MAGNET columns

if __name__ == "__main__":
    import pandas as pd
    data = pd.read_csv("data/CRDC2013_14.csv", encoding = "Latin-1")
    
    ##get more information
    jj_counts = data["JJ"].value_counts()
    sch_status_magnet_counts = data["SCH_STATUS_MAGNET"].value_counts()
    
    #print(jj_counts)
    #print(sch_status_magnet_counts)
    
    #Binary data! We can run a pivot table
    jj_pivot = pd.pivot_table(data, values=["TOT_ENR_M", "TOT_ENR_F"], index="JJ", aggfunc="sum")
    
    sch_status_magnet_pivot = pd.pivot_table(data, values=["TOT_ENR_M", "TOT_ENR_F"], index="SCH_STATUS_MAGNET", aggfunc="sum")
    
    print(jj_pivot)
    print(sch_status_magnet_pivot)
    