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
skript kontroluje sloup 'subtest 1' - 'TMC' a provadi na nich statisticke testy
"""



def age_inervals():
    interval_age = ['6.4 - 6.7', '6.8 - 6.11', '7.0-7.3', '7.4-7.7', '7.8-7.11', '8.0-8.5', '8.6-8.11', '9.0-9.5', '9.6-9.11', '10.0-10.5', '10.6-10.11']

    return interval_age


def calculate_students(df_list):
    """
    calculate the number of students in each group
    """
    students = [len(df) for df in df_list]
   
    return students


def hist_median_bar(value_list):
    plt.bar(age_inervals(),value_list)

    plt.xlabel('Groups')
    plt.ylabel('Median of TMC')
    plt.title('Bar Plot of Data based on age groups')

    plt.show()
    
def hist_median_dots(value_list):
    plt.scatter(list(age_inervals()), list(value_list))

    plt.xlabel('Groups')
    plt.ylabel('Median of TMC')
    plt.title('Bar Plot of Data based on age groups')

    plt.show()
    
def hist_students(df_list):
    plt.scatter(list(age_inervals()), calculate_students(df_list))

    plt.xlabel('Groups')
    plt.ylabel('Number of students')
    plt.title('Bar Plot of Data based on age groups')

    plt.show()
    
def are_data_normally_distributed(data):
    #data_ind = concat_data(data)
    for arr in data:
        #print(arr)
        stat,p = stats.normaltest(arr)
        if p < 0.05:
            return p, False
    return p, True

def are_data_normally_distributed_liliefors(data):
    #data_ind = concat_data(data)
    i = 1
    for arr in data:
        #print(arr)
        stat,p = lilliefors(arr,dist='norm',pvalmethod='table')
        if p < 0.05:
            print("Group ", i, " is not normally distributed")
            i += 1
            return p, False
    return p, True

def concat_data(data):
    #print("concatenate data length: ", len(np.concatenate(data)))
    return np.concatenate(data)
   

def levene_test(data):
    statistic, pvalue = stats.levene(*data)
    #print("Levene Test p-value: ", pvalue)
    if pvalue < 0.05:
        #print("Groups have unequal variances (reject H0) levene")
        return pvalue, False
    return pvalue, True


def bartlett_test(data):
    statistic, pvalue = stats.bartlett(*data)
    #print("Bartlett Test p-value: ", pvalue)
    if pvalue < 0.05:
        #print("Groups have unequal variances (reject H0) bartlett")
        return pvalue, False
    return pvalue, True

def kruskal_wallis_test(data):
    statistic, pvalue = stats.kruskal(*data)
    #print("Kruskal-Wallis Test p-value: ", pvalue)
    if pvalue < 0.05:
        #print("Groups have unequal medians (reject H0) kruskal-wallis")
        return pvalue, False
    return pvalue, True


def anova_test(data):
    statistic, pvalue = stats.f_oneway(*data)
    #print("ANOVA Test p-value: ", pvalue)
    if pvalue < 0.05:
        #print("Groups have unequal medians (reject H0) anova")
        return pvalue, False
    return pvalue, True

def multi_comparasion_test(data):
    tukey_kramer_result = mc.MultiComparison(np.concatenate(data), np.concatenate([[i]*len(group) for i, group in enumerate(data)]))
    tukey_kramer_result = tukey_kramer_result.tukeyhsd()
    df_tu_kr = pd.DataFrame(data=tukey_kramer_result._results_table.data[1:], columns=tukey_kramer_result._results_table.data[0])
    #print(tukey_kramer_result)
    #print(df_tu_kr)
    df_rejected = df_tu_kr[df_tu_kr["reject"] == True]
    #return data frame with rejected values
    print(df_rejected)
    return df_rejected, df_tu_kr

def plot_err_bar_mult_compare(df_rejected, tested_column):
     # Extract data for error bars
    means = df_rejected['meandiff']
    errors = (df_rejected['upper'] - df_rejected['lower']) / 2
    labels = [f"Gr {group1+1} - Gr {group2+1}" for group1, group2 in zip(df_rejected['group1'], df_rejected['group2'])]
    #print(means)
    #print(errors)
    # Plot error bar graph
    x_pos = np.arange(len(labels))
    plt.bar(x_pos, means, yerr=errors, align='center', alpha=0.5, ecolor='black' ,capsize=5)
    plt.xticks(x_pos, labels, rotation=0)
    plt.ylabel('Mean Difference')
    plt.title(tested_column)


    plt.show()
    
    



if __name__ == "__main__":

    # Create a list of the sheet names
    df_list = h.get_multiple_excel_in_df_list()
    #suspicious_columns = ['subtest 1','subtest 2','subtest 3','subtest 4', 'subtest 5', 'subtest 6', 'subtest 7','subtest 8', 'test 1', 'test 2', 'test 3', 'test 4', 'TMC']
    suspicious_columns = ['subtest 7']
    for column in suspicious_columns:
        print(column)
        data = h.get_column_data(df_list,column)
        
            
        #print(data)
        
        #are the data normally distributed?
        
        print("Are the data normally distributed?")
        #are_data_normally_distributed_2(data)
        norm_pv, are_norm_distr = are_data_normally_distributed_liliefors(data)
        print("pvalue: " + str(norm_pv))
        print(are_norm_distr)
        

        if are_norm_distr == False:
            #dispersion matching test(test shodnosti rozptylu) --> data not normally distributed --> levene test
            print("Data are not normally distributed")
            print("Levene test")
            disp_match_pv, disp_match = levene_test(data)
            print("levene pvalue: " + str(disp_match_pv))
            print(disp_match)
        else:
            print("Data are normally distributed")
            # Bartlett test
            print("Bartlett test")
            disp_match_pv, disp_match = bartlett_test(data)
            print("bartlett pvalue: " + str(disp_match_pv))
            print(disp_match)
            
        if disp_match == True and are_norm_distr == False:
            #there are not significant differences in the variances of the samples and the data are not normally distributed
            #kw test
            print("kw test")
            pv, is_stat = kruskal_wallis_test(data) #is_stat = True if there are not significant differences in the medians of the samples False otherwise
            print("kw pvalue: " + str(pv))
            print(is_stat)
        elif disp_match == True and are_norm_distr == True:
            #there are not significant differences in the variances of the samples and the data are normally distributed
            #anova test
            print("anova test")
            pv, is_stat = anova_test(data) #is_stat = True if there are not significant differences in the medians of the samples False otherwise
            print("anova pvalue: " + str(pv))
            print(is_stat)
        elif (disp_match == False and are_norm_distr == True) or (disp_match == False and are_norm_distr == False):
            #kw test
            print("kw test")
            pv, is_stat = kruskal_wallis_test(data) #is_stat = True if there are not significant differences in the medians of the samples False otherwise
            print("kw pvalue: " + str(pv))
            print(is_stat)
            
            
        if is_stat == False:
            #multiple comparison test
            print("Multiple comparison test")
            df_rejected, df_tu_kr = multi_comparasion_test(data)
            if df_rejected.empty:
                continue
            else: #graph printing
                # Create a 11x11 matrix with NaN values
                matrix = np.empty((11, 11))
                matrix[:] = np.nan

                # Fill the matrix with the meandiff values where the group1 and group2 values match the row and column indices
                for idx, row in df_rejected.iterrows():
                    matrix[row['group1'], row['group2']] = -row['meandiff']
                    matrix[row['group2'], row['group1']] = row['meandiff']

                # Create a mask for the NaN values in the matrix
                mask = np.isnan(matrix)

                # Create a heatmap of the matrix with the NaN values masked out
                #labels  = ['6.4 - 6.7', '6.8 - 6.11', '7.0-7.3', '7.4-7.7', '7.8-7.11', '8.0-8.5', '8.6-8.11', '9.0-9.5', '9.6-9.11', '10.0-10.5', '10.6-10.11']
                labels = ['1','2','3','4','5','6','7','8','9','10','11']
                cmap = sns.diverging_palette(240, 10, as_cmap=True)
                sns.heatmap(matrix, mask=mask, cmap=cmap, annot=True, fmt=".2f", linewidths=0.5,linecolor='black',xticklabels=labels, yticklabels=labels,)
                #cmap = YlGnBu
                #plt.xticks(rotation=45)
                plt.title(column)
                plt.xlabel("Skupiny z tabulky 4.1")
                plt.ylabel("Skupiny z tabulky 4.1")



                # Show the plot
                plt.show()
            #plot_err_bar_mult_compare(df_rejected, column)
            # pivot the data
            
            
            
            
            
        """
            cmap = sns.diverging_palette(220, 10, as_cmap=True)
            cmap = cmap.reversed()
            if df_rejected.empty:
                continue

            # Define center for colormap
            vmin = np.min(df_rejected['meandiff'])
            vmax = np.max(df_rejected['meandiff'])
            center = (vmax + vmin) / 2
            

            # Plot heatmap
            sns.set(rc={'figure.figsize':(6,4)})
            print(df_rejected.pivot('group1', 'group2', 'meandiff'))
            sns.heatmap(df_rejected.pivot('group1', 'group2', 'meandiff'), cmap='rocket', center=center, vmin=vmin, vmax=vmax,linewidths=1,linecolor='black')
            new_x_tick_labels  = ['6.4 - 6.7', '6.8 - 6.11', '7.0-7.3', '7.4-7.7', '7.8-7.11', '8.0-8.5', '8.6-8.11', '9.0-9.5', '9.6-9.11', '10.0-10.5', '10.6-10.11']
            plt.xticks(ticks=range(11), labels=new_x_tick_labels)
            
            plt.yticks(ticks=range(11), labels=new_x_tick_labels)



            # Show plot
            plt.show()
            """

    
                
                
    """
                pivoted_df = df_rejected.pivot(index='group1', columns='group2', values='meandiff')

            # create the heatmap using seaborn
            cmap = sns.diverging_palette(220, 10, as_cmap=True)
            cmap = cmap.reversed()
            sns.heatmap(pivoted_df, cmap) #, annot=True --> to show the values in the heatmap ='coolwarm'

            # set the title and axis labels
            plt.title('Mean Difference Heatmap')
            plt.xlabel('Group 2')
            plt.ylabel('Group 1')

            # show the plot
            plt.show()
    
    
    
    
    
    
    
    
        #vypocet distribucni funkce a jeji zobrazeni
    #test
    df_list2 = h.get_multiple_excel_in_df_list()
    data = h.get_column_data(df_list2,1)
    print(data)
    flat_list = [item for sublist in data for item in sublist]
    #vypocet distribucni funkce
    counts, bin_edges = np.histogram(flat_list, bins=20, density=True)
    cdf = np.cumsum(counts)
    
    # Plot the distribution function
    sns.set()
    fig, ax = plt.subplots()
    sns.lineplot(x=bin_edges[1:], y=cdf, drawstyle='steps-post', ax=ax)
    ax.set_xlabel('x')
    ax.set_ylabel('F(x)')
    ax.set_title('Empirical CDF')
    plt.show()
    
    
    
    
    
    
    counts = np.bincount(flat_list)
    dist = np.cumsum(counts) / len(flat_list)
    
    print(dist)
    
    
    
    
    
    
    
    
    
    
     # Create a list to store the median values from the 'TMC' column of each DataFrame
    medians = [df[' TMC'].median() for df in df_list]
    #print(medians)
    # Print the results
    #means = [df[' TMC'].median() for df in df_list]
    #print("Means: " + str(means))

        
    #print(df_list[10].describe())
    
    hist_median_bar(medians)#cim vyssi vek tim nizsi TMC??
    hist_median_dots(medians)
    hist_students(df_list)
        
    #muze to ze cim je dite starsi byt ovlivneno poctem skupin zaku v jednotlivych vekovych kategoriich?
    # nebo naopak cim je mene studentu ve skupine tim vice mohou byt data zkreslena
    print("Number of students in each group: " + str(calculate_students(df_list))) 
    
    #multiple comparison test
    tukey_kramer_result = mc.MultiComparison(np.concatenate(data), np.concatenate([[i]*len(group) for i, group in enumerate(data)]))
    tukey_kramer_result = tukey_kramer_result.tukeyhsd()
    df_tu_kr = pd.DataFrame(data=tukey_kramer_result._results_table.data[1:], columns=tukey_kramer_result._results_table.data[0])
    #print(tukey_kramer_result)
    #print(df_tu_kr)
    df_rejected = df_tu_kr[df_tu_kr["reject"] == True]
    #print(df_rejected)
    
    #try to plot error bar
    # Extract data for error bars
    means = df_rejected['meandiff']
    errors = (df_rejected['upper'] - df_rejected['lower']) / 2
    labels = [f"Gr {group1+1} - Gr {group2+1}" for group1, group2 in zip(df_rejected['group1'], df_rejected['group2'])]
    print(means)
    print(errors)
    # Plot error bar graph
    x_pos = np.arange(len(labels))
    plt.bar(x_pos, means, yerr=errors, align='center', alpha=0.5, ecolor='black' ,capsize=5)
    plt.xticks(x_pos, labels, rotation=0)
    plt.ylabel('Mean Difference')
    plt.title('Group Comparisons')


    plt.show()
    """
    



  
    
    
    
    """
    chci testovat hodnotu TMC pro jednotlive skupiny podle veku
    muzu to udelat pomoci ANOVA? jaky test pouzit?
        1) test na normalitu dat --> pochazi data z normalniho rozdeleni?
            h0: data pochazi z normalniho rozdeleni
            h1: data nejsou z normalniho rozdeleni
            p-value < 0.05 --> zamitam h0 --> pro jednu skupinu nejsou data z normalniho rozdeleni (konkretne skupina 10)
        2) test na rovnost rozptylu --> maji vsechny skupiny stejny rozptyl?
        zvolen levenuv test kvuli neoverene normalite dat --> respektive nejaka data nejsou z NR
        viz prednasky:
            Ověřena normalita dat – Bartlettův test
            Neověřena normalita dat – Leveneův test
            h0: rozptyly jsou stejne
            h1: rozptyly nejsou stejne
            --> p-value > 0.05 --> nezamitam h0
    na zaklade techto dvou testu nemuzu pouzit anova test, jelikoz data nejsou z normalniho rozdeleni
    pouziju tedy kruskal-wallis test:
        kraskal-wallis test:
            h0: vsechny skupiny maji stejny median
            h1: aspon 1 median je jiny
            --> p-value < 0.05 --> zamitam h0 --> aspon 1 median je jiny
                5.756212576444608e-08
    jelikoz muzu zamitnout h0, je potreba provest test mnohonasobneho porovnani abych 
    odhalil mezi jakymi skupinami jsou vyznamne rozdily
            group1  group2  meandiff   p-adj    lower   upper  reject
    6        0       7   -7.0040  0.0471 -13.9648 -0.0431    True
    7        0       8  -11.2688  0.0001 -18.6636 -3.8740    True
    8        0       9   -9.7688  0.0009 -17.0856 -2.4521    True
    9        0      10   -8.0244  0.0276 -15.6033 -0.4455    True
    16       1       8   -8.2667  0.0031 -14.9076 -1.6257    True
    17       1       9   -6.7667  0.0362 -13.3206 -0.2127    True
    24       2       8   -6.9071  0.0140 -13.0680 -0.7462    True
    31       3       8   -7.7564  0.0048 -14.1555 -1.3573    True
    37       4       8   -8.0702  0.0018 -14.3288 -1.8116    True
    38       4       9   -6.5702  0.0257 -12.7363 -0.4040    True
    42       5       8   -8.1146  0.0010 -14.2094 -2.0198    True
    43       5       9   -6.6146  0.0172 -12.6144 -0.6147    True

    z prvniho radku napriklad vim ze prumer skupiny 0 je vetsi nez prumer skupiny 7 o 7.0040
        






  
    
    for data_ind in data:
        stat, p = stats.normaltest(data_ind) #lilieforce test
        if p > 0.05:
            print("The data is likely normally distributed.")
        else:
            print("The data is not likely normally distributed.")
            print("p-value: " + str(p))





 #Dispersion matching test - test shodnosti rozptylu
    #levenuv test kvuli neoverene normalite dat --> respektive nejaka data nejsou z NR
    statistic, pvalue = stats.levene(*data)
    print("Levene Test Statistic: ", statistic)
    print("Levene Test p-value: ", pvalue)

    if pvalue > 0.05:
        print("Groups have equal variances (fail to reject H0) levene")
    else:
        print("Groups have unequal variances (reject H0) levene")
        
    statistic, pvalue1 = stats.kruskal(*data)
    if pvalue1 < 0.05:
        print("Reject the null hypothesis (Kruskal-Wallis H-test)")
        print("kruskal pvalue: " + str(pvalue1))
        
        
    #if data are not normally distributed, use non-parametric test
  
        
   

    # Perform the ANOVA
    f_value, p_value = stats.f_oneway(*data)
    #print("F-value:", f_value) #5.306704796472548
    print("P-value:", p_value) #1.645089307056581e-07



    
    """


