import pandas as pd
import helpers as h
import numpy as np
import math

"""
timti skriptem kontroluji zda radky v ruznych sekcich tabulky maji spravne hodnoty
- zda maji spravne hodnoty v testech = vsechny testy nejsou 0
- zda maji spravne hodnoty v subtestech = vsechny subtesty nejsou 0

pokud by totiz meli 0, nemohu vyhodnotit zda tam 0 opravdu je nebo jestli to je chyba
"""




def get_indexes_with_missing_values(data,from1 ,to):
    """
    returns indexes of rows where values are missing
    """
    df = data.iloc[:,from1:to]#get only the columns with specified area
    #print(df)
    sum = df.sum(axis=1,numeric_only=True,skipna=True) #sum the rows ,numeric_only=True
    #print(sum)
    sum_frame = pd.DataFrame(sum, columns = ['sum']) #create a new dataframe with the sum
    sum_frame = sum_frame[sum_frame['sum'] == 0] #get the rows where the sum is 0
    
    return sum_frame.index.values.tolist() #return the indexes of the rows where the sum is 0


def testing_TMC(data):
    """
    returns the indexes of rows where the TMC is 0 wheter tests and subtests are not 0
    """
    df1 = data.iloc[:,58:70]#get only the columns with specified area
    sum = df1.sum(axis=1,numeric_only=True)
    sum_frame = pd.DataFrame(sum, columns = ['sum']) #create a new dataframe with the sum
    sum_frame = sum_frame[sum_frame['sum'] != 0] #get the rows where the sum is 0
    
    df_sum_tmc = pd.concat([sum_frame,data[' TMC']],axis=1)
    df_sum_tmc = df_sum_tmc[(df_sum_tmc[' TMC'] == 0) & (df_sum_tmc['sum'] != 0)]
    return df_sum_tmc.index.values.tolist()


def write_to_file(filename,excel_data,ind):
    data = excel_data.copy()
    indexes = ind
    #print(indexes)
    indexes_int = [int(i) for i in indexes]
    #print(indexes_int)
    data = data.iloc[indexes_int,:] #get the rows with missing tests
    #print(data)
    df_tests =  h.reindex_df(data)
    print(df_tests)
    df_tests.to_csv('./unvalid_data/'+filename)
    

if __name__ == '__main__':
    excel_data = h.get_excel_data('Data_1_11_2022_anonymizovana_data.xlsx', 'List1') #220816_Datova_matice_upravena.xlsx -> puvodni stara matice
    
    
    #tmc is 0 when tests and subtests are not null --> tmc should be number not null or 0
    ind4 = testing_TMC(excel_data)
    print(ind4)
    write_to_file('tmc_is_zero.csv',excel_data,ind4)
    
    
    #tests missing columns --> [67:70] --> tezko rict, v podstate stejny jako subtests
    ind3 = get_indexes_with_missing_values(excel_data,67,70)
    print(ind3)
    write_to_file('tests1-4_missing.csv',excel_data,ind3)
    
    
    
    #subtests missing columns --> [58:66]
    ind2 = get_indexes_with_missing_values(excel_data,58,66)
    print(ind2)
    write_to_file('subtests_missing.csv',excel_data,ind2)
    
    
    
    #missing tests --> everything is missing
    ind1 = get_indexes_with_missing_values(excel_data,5,58)
    print(ind1)
    write_to_file('missing_tests.csv',excel_data,ind1)
    
    
    #
    
    
    #some tests are missing
    """
    prazdno z duvodu toho ze ja proste nevim, zda ten clovek opravdu dostal xkrat 0 nebo jestli to je chyba
    """
    
    
    