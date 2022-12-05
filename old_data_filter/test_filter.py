import pandas as pd
import helpers as h
import numpy as np
import math






def get_df_with_missing_tests(data):
    """
    returns indexes of rows where tests are missing
    """
    df = data.iloc[:,5:58]#get only the columns with test results
    sum = df.sum(axis=1) #sum the rows
    sum_frame = pd.DataFrame(sum, columns = ['sum']) #create a new dataframe with the sum
    sum_frame = sum_frame[sum_frame['sum'] == 0] #get the rows where the sum is 0
    
    return sum_frame.index.values.tolist() #return the indexes of the rows where the sum is 0
    
    






if __name__ == '__main__':
    excel_data = h.get_excel_data('220816_Datova_matice_upravena.xlsx', 'List1')
    
    #missing tests --> everything is missing
    data = excel_data.copy()
    indexes = get_df_with_missing_tests(data)
    indexes_int = [int(i) for i in indexes]
    data = data.iloc[indexes_int,:] #get the rows with missing tests
    df_tests =  h.reindex_df(data)
    df_tests.to_csv('./csv_bad_data/missing_tests.csv')
    
    
    #some tests are missing
    """
    prazdno z duvodu toho ze ja proste nevim, zda ten clovek opravdu dostal xkrat 0 nebo jestli to je chyba
    """