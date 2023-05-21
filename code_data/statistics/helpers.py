import pandas as pd
import numpy as np
from statsmodels.stats.diagnostic import lilliefors
from scipy.stats import chisquare, norm

#test
import seaborn as sns
import matplotlib.pyplot as plt
import math




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

def get_multiple_excel_in_df_list():
    """
    reurns all sheets in excel file as list of data frames
    """
    sheet_names = ['Group1', 'Group2', 'Group3', 'Group4', 'Group5', 
                    'Group6','Group7', 'Group8', 'Group9','Group10','Group11'
                ]
    # Combine the data into a single DataFrame
    df_list = []
    for sheet in sheet_names:
        df = get_excel_data('../age_groups/Student_groups_by_age_valid_2.xlsx', sheet)
        df.drop(['Unnamed: 0'], axis=1) # delete column 'Unnamed: 0'
        df_list.append(df)
    return df_list

def get_column_data(df_list, column_name):
    """
    get data from column in data frame
    """
    data = [df[column_name].values for df in df_list]
    return data

def lilie_forse(vec):
    return  lilliefors(vec,dist='norm',pvalmethod='table')
    #[ks_x,p_x] = lilliefors(x,dist='norm',pvalmethod='table')

    
"""
if some of vectors is not normally distributed, return False
go through all columns in data frame
"""
def are_normally_distributed(df):
    print(df)
    for (columnName, columnData) in df.iteritems():
        #print('Column Name : ', columnName)
        #print('Column Contents : ', len(list(columnData.values)))
        [ks,p] = lilie_forse(columnData.values)
        if p < 0.05:
           return False, p
       
    return True,p






"""if __name__=="__main__":
    #sloupec = F, test = 1 v excelu
    F_1 = [3, 3, 3, 3, 3, 3, 3, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 1, 3, 3, 2, 3, 3, 3, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 2, 3, 3, 3, 2, 3, 3, 3, 3, 3, 2, 3, 2, 2, 3, 3, 2, 2, 3, 2, 3, 3, 3, 3, 2, 3, 3, 3, 3, 3, 3, 2, 3, 3, 3, 3, 2, 3, 3, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 2, 3, 3, 2, 2, 3, 3, 3, 3, 2, 3, 2, 3, 3, 2, 2, 3, 2, 3, 3, 2, 2, 3, 3, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 2, 2, 2, 3, 3, 3, 2, 3, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 3, 3, 3, 2, 3, 3, 2, 3, 3, 3, 3, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 3, 3, 3, 3, 3, 2, 3, 3, 3, 3, 3, 3, 2, 0, 3, 3, 3, 3, 2, 3, 3, 2, 2, 3, 3, 3, 3, 2, 2, 3, 2, 1, 2, 3, 3, 3, 3, 3, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 3, 3, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 3, 3, 3, 2, 3, 2, 3, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 2, 3, 3, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 2, 3, 2, 3, 3, 3, 3, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 3, 3, 3, 3, 3, 3, 2, 3, 3, 3, 3, 2, 2, 3, 3, 3, 3, 3, 3, 2, 3, 3, 3, 3, 3, 3, 3, 2, 3, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 3, 3, 3, 3, 3, 2, 3, 3, 3, 3, 3, 3, 3, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 3, 3, 3, 3, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 3, 2, 3, 3, 3, 3, 3, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 3, 3, 2, 3, 3, 3, 3, 3, 2, 3, 2, 3, 3, 3, 2, 3, 3, 3, 3, 3, 3, 3, 3, 2, 3, 3, 3, 2]
    print(lilie_forse(F_1))
"""




def chi_square_test_normality(data):
    # Calculate the mean and standard deviation of the data
    mu = np.mean(data)
    sigma = np.std(data)

    # Calculate the expected frequencies for a normal distribution
    expected = np.array([len(data) * (norm.cdf((i - mu) / sigma) - norm.cdf((i - mu) / sigma)) for i in data])
    print(expected)
    
    # Add a small constant to avoid zero values
    expected += 0.001

    # Calculate the observed frequencies
    observed = np.histogram(data, bins=len(data))[0]

    # Calculate the chi-square statistic and p-value
    chi_sq_statistic, p_value = chisquare(observed, expected)

    return chi_sq_statistic, p_value


def chi_square_test_normality2(data):
    # Calculate the mean and standard deviation of the data
    mu = np.mean(data)
    sigma = np.std(data)

    # Calculate the expected frequencies for a normal distribution
    expected = np.array([len(data) * (norm.cdf((i + 0.5 - mu) / sigma) - norm.cdf((i - 0.5 - mu) / sigma)) for i in data])
    
    
    # Add a small constant to avoid zero values
    #expected += 0.001
    #print(expected)

    # Calculate the observed frequencies
    observed = np.histogram(data, bins=len(data))[0]
    #observed += 0.001
    print(observed)

    # Calculate the chi-square statistic and p-value
    chi_sq_statistic, p_value = chisquare(observed, expected)

    return chi_sq_statistic, p_value


if __name__=="__main__":

    #https://analyticsindiamag.com/goodness-of-fit-python-guide/
    path = 'https://raw.githubusercontent.com/RajkumarGalaxy/dataset/master/Tabular/bulb_life.csv'
    data = pd.read_csv(path)
    print(data)
    #sns.histplot(data=data, x='life', bins=8)
    #plt.show()
    # mean and standard deviation of given data
    mean = np.mean(data['life'])
    std = np.std(data['life'])
    bins = 8
    interval = []
    for i in range(1,9):
        val = norm.ppf(i/bins, mean, std)
        interval.append(val)
    print(interval)
    interval.insert(0, -np.inf)
    print(interval)
    
    df = pd.DataFrame({'lower_limit':interval[:-1], 'upper_limit':interval[1:]})
    print(df)
    
    life_values = list(sorted(data['life']))
    print(life_values)
    df['obs_freq'] = df.apply(lambda x:sum([i>x['lower_limit'] and i<=x['upper_limit'] for i in life_values]), axis=1)
    df['exp_freq'] = 5
    print(df)
    print(chisquare(df['obs_freq'], df['exp_freq']))
    
    
    
    x =[10, 0, 12, 10, 10, 10, 12, 12, 11, 10, 11, 12, 3, 7, 10, 9, 12, 0, 11, 0, 12, 12, 0, 11, 0, 0, 8, 11, 0, 10, 5, 12, 11, 9, 12, 10, 9, 12, 12, 12, 10, 11, 10, 10, 12, 11, 12, 11, 12, 9, 12, 10, 11, 0, 12, 12, 9, 5, 0, 12, 12, 12, 6, 11, 10, 11, 12, 10, 10, 8, 12, 11, 10, 11, 11, 9, 9, 12, 11, 12, 11, 12, 0, 12, 6, 10, 12, 11, 11, 12, 11, 10, 11, 10, 0, 10, 12, 12, 11, 10, 12, 11, 11, 12, 12, 10, 9, 10, 4, 12, 10, 0, 10, 11, 12, 10, 10, 12, 11, 12, 12, 9, 12, 10, 11, 12, 10, 10, 11, 11, 12, 10, 9, 11, 12, 10, 11, 10, 9, 12, 11, 12, 12, 12, 9, 11, 10, 9, 11, 11, 11, 12, 12, 10, 11, 0, 0, 9, 11, 12, 11, 10, 12, 0, 10, 12, 11, 11, 11, 11, 11, 10, 10, 9, 12, 10, 11, 12, 11, 10, 11, 12, 12, 10, 11, 12, 10, 11, 12, 12, 12, 11, 11, 12, 12, 12, 12, 11, 12, 11, 11, 11, 12, 11, 10, 12, 12, 12, 11, 9, 11, 10, 0, 9, 12, 12, 8, 12, 12, 0, 12, 12, 11, 12, 12, 10, 0, 11, 11, 11, 11, 12, 11, 11, 11, 12, 11, 10, 12, 11, 12, 12, 11, 10, 12, 9, 12, 12, 6, 12, 11, 11, 12, 12, 12, 11, 11, 10, 12, 12, 11, 12, 12, 10, 11, 12, 10, 12, 9, 12, 12, 11, 11, 12, 7, 12, 12, 11, 12, 12, 12, 12, 11, 12, 10, 12, 12, 10, 10, 11, 12, 10, 12, 12, 11, 11, 9, 12, 10, 12, 12, 10, 8, 12, 10, 12, 12, 11, 12, 11, 11, 12, 12, 12, 12, 12, 12, 11, 11, 12, 9, 10, 11, 12, 12, 10, 11, 12, 12, 12, 11, 12, 12, 12, 12, 11, 10, 10, 10, 12, 10, 11, 10, 10, 11, 10, 12, 12, 10, 12, 12, 12, 12, 12, 10, 12, 10, 11, 11, 12, 12, 10, 12, 12, 11, 9, 11, 10, 10, 12, 11, 11, 12, 11, 12, 9, 12, 12, 12, 9, 12, 12, 12, 12, 10, 11, 12, 12, 10, 11, 12, 11, 0, 11, 12, 12, 11, 12, 12, 11, 12, 12, 11, 11, 10, 6, 8, 12, 12, 11, 11, 12, 11, 10, 10, 12, 10, 9, 11, 12, 10, 11, 10, 10, 12, 12, 12, 12, 11, 12, 12, 11, 12, 12, 12, 10, 11, 11, 9, 11, 10, 12, 8, 10, 12, 12, 12, 12, 12, 12, 0, 12, 11, 11, 12, 12, 12, 12, 12, 9, 12, 12, 11, 12, 12, 12, 11, 10, 11, 11, 11, 12, 11, 9, 12, 11, 9, 10, 11, 10, 12, 11, 12, 12, 12, 12, 12, 12, 11, 11, 10, 9, 11, 10, 10, 11, 12, 12, 0, 12, 10, 12, 12, 10, 12, 11, 12, 12, 11, 12, 12, 10, 12, 11, 12, 12, 10, 0, 11, 11, 12, 11, 11, 10, 12, 12, 11, 10, 11, 11, 12, 10, 12, 10, 9, 11, 10, 9, 12, 12, 12, 11, 8, 11, 11, 12, 11, 12, 12, 11, 11, 11, 12, 12, 12, 11, 12, 8, 10, 11, 12, 12, 12, 12, 11, 6, 12, 11, 11, 11, 12, 11, 11, 11, 12, 11, 12, 11, 11, 12, 10, 12, 12, 11, 11, 12, 10, 10, 12, 12, 11, 12, 10, 11, 11]
    mean = np.mean(x)
    std = np.std(x)
    bins = 595 / 5 #musi jich byt aspon 5
    interval = []
    for i in range(1,596):
        val = norm.ppf(i/bins, mean, std)
        interval.append(val)
    print(interval)
    interval.insert(0, -np.inf)
    interval = [x for x in interval if not math.isnan(x)]

    df = pd.DataFrame({'lower_limit':interval[:-1], 'upper_limit':interval[1:]})
    print(df)
    x_values = list(sorted(x))
    print(len(x_values))
    df['obs_freq'] = df.apply(lambda x:sum([i>x['lower_limit'] and i<=x['upper_limit'] for i in life_values]), axis=1)
    df['exp_freq'] = 0
    print(df)
    print(chisquare(df['obs_freq'], df['exp_freq']))

    


