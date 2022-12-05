import pandas as pd
import numpy as np
import matplotlib.pyplot as plt












if __name__ == '__main__':
    excel_data = pd.read_excel('Data_1_11_2022_anonymizovana_data.xlsx',sheet_name='DATA_OUT')
    print(excel_data)
    year_tmc_data = excel_data.loc[:,['třída',' TMC']]
    print(year_tmc_data)