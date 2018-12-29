##Reads the content of the CRDC2013_14content.csv file and observes the column names

if __name__ == "__main__":
    import pandas as pd
    contents = pd.read_csv("dCRDC2013_14content.csv")
    print(contents.info)
    print(contents.head())
    ## A lot of columns! It looks like the header is not the only the column names but the column descriptions. Every row represents a column. We see two interesting ones: "JJ" and "SCH_STATUS_MAGNET"