
import pandas as pd
from scipy import stats
import helpers as h
import matplotlib.pyplot as plt
import statsmodels.stats.multicomp as mc
import numpy as np
import seaborn as sns
from statsmodels.stats.diagnostic import lilliefors
import matplotlib
"""
skript slouzi pro lepsi zobrazeni dat v bp --> zobrazuje sloupcovy graf pro kazdy subtest, test a tmc kde zobrazuje prumery dosazene v jednotlivych skupinach

vysledkem je nasledujici pole:
subtest 1
[8.612903225806452, 8.88888888888889, 8.4, 7.480769230769231, 9.333333333333334, 9.921875, 9.26984126984127, 9.73972602739726, 8.803921568627452, 7.962962962962963, 8.977777777777778]

kde je subtest1 je nazev testovaneho sloupce, nasleduje pole hodnot, ktere jsou prumerem dosazene v jednotlivych skupinach v jednotlivych listech souboru pro dany subtest
soubor .xlsx ze kterehou josu brana data ma 11 listu, takze je 11 hodnot v poli
[8.612903225806452, 8.88888888888889, 8.4, 7.480769230769231, 9.333333333333334, 9.921875, 9.26984126984127, 9.73972602739726, 8.803921568627452, 7.962962962962963, 8.977777777777778]
[       Group1,          Group2,    Group3, Group4,              Group5,          Group6,        Group7,         Group8,            Group9,           Group10,            Group11]
"""


if __name__ == "__main__":

    # Create a list of the sheet names
    df_list = h.get_multiple_excel_in_df_list()
    suspicious_columns = ['subtest 1','subtest 2','subtest 3','subtest 4', 'subtest 5', 'subtest 6', 'subtest 7','subtest 8', 'test 1', 'test 2', 'test 3', 'test 4', 'TMC']
    #suspicious_columns = ['subtest 2']
    mean_data = []
    for column in suspicious_columns:
        print(column)
        data = h.get_column_data(df_list,column)
        #print(data)
    
    
        for list_i in data:
            mean_data.append(np.mean(list_i))
        

        print(mean_data)
        x = range(1, 12)
        plt.bar(x, mean_data)

        plt.xlabel('Age groups')
        plt.ylabel('Mean')
        plt.title('Mean of ' + column)

        plt.xticks(x)
        plt.show()
        mean_data = []
        print()
       