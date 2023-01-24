import pandas as pd
import numpy as np
import helpers as h




def get_NaT_birth_date(data):
    """
    Return the column where the birth date is NaT
    """
    b_date = data.loc[:,:]
    b_date = b_date[b_date['datum narození'].isnull()]
    
    return b_date

def get_NaT_test_date(data):
    """
    Return the column where the test date is NaT
    """
    t_date = data.loc[:,:]
    t_date = t_date[t_date['datum testu'].isnull()]
    
    return t_date



if __name__ == '__main__':
    excel_data = h.get_excel_data('Data_1_11_2022_anonymizovana_data.xlsx', 'List1')
    print(excel_data)
    df1 = get_NaT_birth_date(excel_data)
    df1_indexes_same_as_excel = h.reindex_df(df1)
    print(df1_indexes_same_as_excel)
    df1_indexes_same_as_excel.to_csv('./csv_bad_data/birth_date_missing.csv')
    
    #df2 = emtpy cell with day of test
    df2 = get_NaT_test_date(excel_data)
    df2_indexes_same_as_excel = h.reindex_df(df2)
    print(df2_indexes_same_as_excel)
    df2_indexes_same_as_excel.to_csv('./csv_bad_data/test_date_missing.csv')
