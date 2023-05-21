import pandas as pd
import helpers as h
import os

"""

"""

"""
def delete_rows(df1, df2):
  
   #Delete rows from df1 which are in df2
    
    df_merged = df1.merge(df2, indicator=True, how='outer')
    print(df_merged)
    df_left_only = df_merged[df_merged['_merge'] == 'left_only']
    df_dropped = df_left_only.drop(['_merge'], axis=1, inplace=True) 
    return df_dropped
"""


    



if __name__ == '__main__':
    excel_data = h.get_excel_data('Data_1_11_2022_anonymizovana_data.xlsx', 'List1')
    csv_data = pd.read_csv('./unvalid_data/max_value_exceeded.csv')
    rows = csv_data.radek.tolist()
    #have to remove duplicates from original list!!!!!!!!
    unique_rows = list(set(rows))
   # print(len(unique_rows)) #--> 41
    for row in unique_rows:
        excel_data = excel_data.drop([row], axis=0)
    #print(excel_data)
    excel_data.to_excel('./excel_files/Data_Filtered.xlsx', index=True)
    
    
   