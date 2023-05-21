import pandas as pd
import helpers as h
import re
import csv

"""
methods of this scripts are used for filtering data in two ways:
1) filter data where value of column is not numeric number but is string for example which is not possible
2) filter data where value of column is bigger than max value --> not for every column, in some tests max_values are not defined
    also check if value is lesser than zero --> min_value is zero in every column
"""

def value_filter(df, col_name, max_value):
    """
    Return the column where the value is bigger than max_value
    """
    df_copy = df.copy() #musim pracovat s kopii abych si neprepisoval puvodni data
    df_copy[col_name] = pd.to_numeric(df_copy[col_name], errors='coerce')
    col = df_copy.loc[:,col_name]
    col = col[(col > max_value) | (col < 0)]
    
    return df.iloc[col.index]



def get_strings(df, col_name):
    """
    Return the column where the value is not numeric and put it into NaN value
    """
    col = df.loc[:,col_name]
    col = pd.to_numeric(col, errors='coerce') #put nan where values are not numeric
    result = pd.isna(col) #dataframe where is True where is NaN
    nan_index = result[result == True].index.tolist() #list of indexes where is NaN
   
    
    #print(df.iloc[nan_index])
    return df.iloc[nan_index] #return rows from original dataframe where is NaN, aka not numeric values






if __name__ == '__main__':
    df = h.get_excel_data('Data_1_11_2022_anonymizovana_data.xlsx', 'List1')
    #print(value_filter(df,48, 1000000))
   # df2 = df[37]
    #print(df2.describe())
   




    
   
    
   #test for non numeric values
    
    #poznamka pro oponenta (update 8.5.2023): tento blok kodu (#TEST FOR NON NUMERIC VALUES) zrejme nebude fungovat na vstupni matici 'Data_1_11_2022_anonymizovana_data.xlsx' ,
    # jelikoz jsem v ramci opravy souboru pro dalsi deleni zmenil datovy typ u nalezene bunky na 'vlastni (jde o ciselny typ)', coz zpusobilo ze se vsechny bunky s puvodne 
    # nevalidnimi daty staly validnimi
    #tato zmena byla provedena nekdy v prosinci 2022 kdyz byl tento kod programovan a nekladl jsem duraz na to, ze pokud data zmenim, vystupy mohou byt jine
    # momentalne se nalezena hodnota tedy tvari jako cislo: 44264.0
    # bohuzel se mi tento postup nepodarilo vratit tak aby to sedelo s tim co je napsane v praci a dalo se to dale otestovat,
    #kvuli tomu je zde uveden jedoduchy testovaci data frame, kterym lze metodu pripadne otestovat:
    """
    data = {'test1': ['abc', 3, 'ghi'],
    'test2': ['xyz', 3, 2]}

    df_test = pd.DataFrame(data)
    print(df_test)
    print(get_strings(df_test, 'test1'))
    """
    
    
   #TEST FOR NON NUMERIC VALUES
    rows_with_nnv = pd.DataFrame() #dataframe where will be rows with non numeric values
    for i in range(1,54):
        if not get_strings(df, i).empty:
            print(get_strings(df, i))
            rows_with_nnv = pd.concat([rows_with_nnv, get_strings(df, i)])
        
    #print(h.reindex_df(rows_with_nnv)) #row where is non numeric value as df
    reindex_df = h.reindex_df(rows_with_nnv)
    print(reindex_df)
   # reindex_df.to_csv('./unvalid_data/non_numeric_values.csv')# write to csv
    
    
    #test for max values
    list_max_values = [3, 3, 1000000, 1000000, 12, 12, 12,
                       4, 5, 6, 6, 5, 5, 5, 6,
                       80, 20, 30, 50, 15,
                       4, 5, 5, 5, 5, 10, 10,
                       10, 6, 10, 10, 6, 10, 10, 10, 10,
                       1000000, 1000000, 1000000, 1000000, 1000000,
                       5, 5, 5, 5, 10, 10, 5,
                       1000000, 1000000, 1000000, 1000000, 60 #, 60
                       ] #1000000 = undefined max value
    
    filtered = pd.DataFrame()
    row = ''
    column = 'sloupec(nazev),radek\n'
    for i in range(0,52):         
        if not value_filter(df, i+1, list_max_values[i]).empty:
            row = str(h.reindex_df(value_filter(df, i+1, list_max_values[i])).index)
            row = re.findall(r'\d+', row)
            x = [int(x) for x in row]
            for item in x:
                column += str(i+1) + ',' + str(item) + '\n'
                
    list_max_values_subtest =[41, 40, 45, 24, 37, 52, 39, 42]
    col_name = "subtest "
    for i in range(len(list_max_values_subtest)):
        if not value_filter(df, col_name+str(i+1), list_max_values_subtest[i]).empty:
            row = str(h.reindex_df(value_filter(df, col_name+str(i+1), list_max_values_subtest[i])).index)
            row = re.findall(r'\d+', row)
            x = [int(x) for x in row]
            for item in x:
                column += str(col_name.strip()+str(i+1)) + ',' + str(item) + '\n'
            
           
   # print(column) 
    #with open("./unvalid_data/max_value_exceeded.csv", "w") as text_file:
        #text_file.write(column)
    

        
   
   
