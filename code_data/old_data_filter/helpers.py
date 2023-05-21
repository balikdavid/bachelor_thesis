import pandas as pd
import numpy as np

def reindex_df(df):
    """
    reindex data frame for same indexing as excel file
    reindex all indexes by 2 [0 --> 2, 1 --> 3, ...]
    """
    indexes = df.index+2
    ind = indexes.tolist()
    list_string = map(str, ind)
    l_str2 = list(list_string)
    newdf = df.reindex(l_str2)
    df.index = newdf.index
    
    return df

def get_excel_data(filename: str, sheetname: str) -> pd.DataFrame:
    """
    read excel file and return data frame
    """
    return  pd.read_excel(filename, sheet_name= sheetname)
    