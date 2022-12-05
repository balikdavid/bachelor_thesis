import pandas as pd
import numpy as np
import matplotlib.pyplot as plt






if __name__ == '__main__':
    excel_data = pd.read_excel('Data_1_11_2022_anonymizovana_data.xlsx',sheet_name='List1')
    print(excel_data)
    
    
    ex2 = excel_data.copy()

    
    
    #with pd.ExcelWriter('Data_1_11_2022_anonymizovana_data.xlsx',mode='a',engine='openpyxl',date_format = 'yyyy mm dd', 
                       # datetime_format='yyyy mm dd') as writer:  
        #ex2.to_excel(writer, sheet_name='test_append')
    with pd.ExcelWriter('test1.xlsx',date_format = 'yyyy mm dd', datetime_format='yyyy mm dd') as writer:
        ex2.to_excel(writer, sheet_name='test1')


