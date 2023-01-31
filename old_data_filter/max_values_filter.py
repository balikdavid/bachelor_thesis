import pandas as pd
import helpers as h
import re

"""
methods of this scripts are used for filtering data in two ways:
1) filter data where value of column is not numeric number but is string for example which is not possible
2) filter data where value of column is bigger than max value --> not for every column, in some tests max_values are not defined
    also check if value is lesser than zero --> min_value is zero in every column

"""


"""
TODO:
kdyz mam v tabulce string tak ho nemuzu porovnavat jako <> cislo, musim ho nejak prevest na cislo nebo na nan
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
    df = h.get_excel_data('220816_Datova_matice_chybna.xlsx', 'List1')
   # print(value_filter(df,1, 3))
    
    #test for non numeric values
    rows_with_nnv = pd.DataFrame() #dataframe where will be rows with non numeric values
    for i in range(1,53):
        if not get_strings(df, i).empty:
            rows_with_nnv = pd.concat([rows_with_nnv, get_strings(df, i)])
            
    #print(rows_with_nnv) #row where is non numeric value as df 
    (rows_with_nnv).to_csv('./unvalid_data/non_numeric_values.csv') #write to csv  
    
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
    column = 'sloupec, radek/radky\n'
    for i in range(0,52):         
        if not value_filter(df, i+1, list_max_values[i]).empty:
            row = str((value_filter(df, i+1, list_max_values[i])).index)
            row = re.search(r'\[(.*)\]', row)
            result = row.group(1)
            index_list = [int(x) for x in result.split(', ')]
            #print(index_list)
            column += str(i+1) + ',' + str(index_list) + '\n'
           
    #print(column + "\n" + "k indexu radku pricti + 2") 
    with open("./unvalid_data/max_value_exceeded.csv", "w") as text_file:
        text_file.write(column) # tady je potreba ke kazdemu indexu pricist + 2 protoze to ma proste jine nastaveni nez druha excel tabulka
   

    

        
   
   
