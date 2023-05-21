
# Importing libraries
import statsmodels.api as sm
import helpers as h
import pandas as pd
from statsmodels.formula.api import ols
from scipy import stats
#import scikit_posthocs as sp
import numpy as np
import statsmodels.stats.multicomp as mc
#import pingouin as pg
from statsmodels.stats.multicomp import pairwise_tukeyhsd
import matplotlib.pyplot as plt
import seaborn as sns





"""
zdroj: https://towardsdatascience.com/anova-tukey-test-in-python-b3082b6e6bda
nefunguje zatim test na normalni rozdeleni --> jinak pak to razeni jakej test se ma udelat
je ok --> to musi sedet s diagramem
"""
def multi_comparasion_test(data,groups):
    tukey_kramer_result = mc.MultiComparison(data,groups)
    tukey_kramer_result = tukey_kramer_result.tukeyhsd()
    df_tu_kr = pd.DataFrame(data=tukey_kramer_result._results_table.data[1:], columns=tukey_kramer_result._results_table.data[0])
    #print(tukey_kramer_result)
    #print(df_tu_kr)
    df_rejected = df_tu_kr[df_tu_kr["reject"] == True]
    #return data frame with rejected values
    print(df_rejected)
    return df_rejected, df_tu_kr

def levene_test(data):
    statistic, pvalue = stats.levene(data)
    #print("Levene Test p-value: ", pvalue)
    if pvalue < 0.05:
        #print("Groups have unequal variances (reject H0) levene")
        return pvalue, False
    return pvalue, True


def bartlett_test(data):
    statistic, pvalue = stats.bartlett(data)
    #print("Bartlett Test p-value: ", pvalue)
    if pvalue < 0.05:
        #print("Groups have unequal variances (reject H0) bartlett")
        return pvalue, False
    return pvalue, True


if __name__ == "__main__":


    df_list = h.get_multiple_excel_in_df_list()
    #suspicious_columns = ['subtest 1','subtest 2','subtest 3','subtest 4',
     #                        'subtest 5', 'subtest 6', 'subtest 7','subtest 8', 
      #                       'test 1', 'test 2', 'test 3', 'test 4', 'TMC']

    suspicious_columns = [ 'subtest 1']
    for i in range(len(df_list)):
        df_list[i] = df_list[i].assign(group = 'gr'+str(i+1))
       # print(df_list[i][['TMC','group']])
        #res = pd.concat([df_list[i]],ignore_index=True, names=[' TMC','group'])
    
    data = pd.concat([df for df in df_list],ignore_index=True)
    #print(data)
    data.columns = data.columns.str.replace(' ', '')
    #print(data)

    for column in suspicious_columns:
        print(column)
        col = column.replace(" ", "")
        data2 = data[['gender','group',col]]
        print(list(data2[col]))
       
        #print("pinguin friedman test")
        
        #print(pg.friedman(data=data2, dv=col, within="group", subject="gender"))
        #print(pg.friedman(data=data2, dv=col, within="gender", subject="group"))
        #print()
        #pg.friedman(data=data2, dv=col, within=['group', 'gender'], subject='gender')
        
        
        #test for normality
        
        k,p_value = h.lilie_forse(data2[col])
        
        if p_value < 0.05:
            print("data are not normally distributed: " + str(p_value))
            normality = False
        else:
            print("data are normally distributed")
            normality = True
            
        #blok vyrazen --> zrychleni vypoctu, pvalue je stejna jako ve skriptu stat_test.py, jelikoz jsou testovana uplne stejna data a tim padem nema smysl testovat tato data znovu
        if normality == False:
            #levene
            print("levene")

        else:
            #bartlett
            print("bartlett")
            
                        
        """    
        if normality == False:
            #Friedman test --> data are not normally distributed
            groups = []
            for i in list(data2.group):
                newi = i[2:] #remove 'gr' from group name take only number of group because friedman test needs only numbers
                #print(newi)
                groups.append(newi)
                
            #print(groups)
                
            genders = []
            for i in list(data2.gender):
                if i == 'M':
                    i = 0
                elif i == 'F':
                    i = 1
                genders.append(i)
            #print(genders)
            
            res2 = stats.friedmanchisquare(genders, groups, data2[col]) #["TMC"]

            """
            
       #else:
        # Performing two-way ANOVA
        print()
        print(col)
        print(data2)
        data2.reset_index(inplace=True)

        model = ols(
        '{} ~ C(gender) + C(group) +\
        C(gender):C(group)'.format(col), data=data2).fit()
        res = sm.stats.anova_lm(model, typ=2)
        print(res)
        
        
        data2['combination'] = data2.gender + " / " + data2.group
       # data2['gender_binary'] = pd.get_dummies(data2['gender'])['F']
        #data2['combination_cat'] = pd.Categorical(data2['combination'])


        print(data2)
        
        #perfrom multiple pairwise comparison (Tukey HSD)
        m_comp = pairwise_tukeyhsd(endog=data2[col], groups=data2['combination'], alpha=0.05)
        print(m_comp)
        
        # coerce the tukeyhsd table to a DataFrame
        tukey_data = pd.DataFrame(data=m_comp._results_table.data[1:], columns = m_comp._results_table.data[0])
            
        #group1_comp =tukey_data.loc[tukey_data.reject == True].groupby('group1').reject.count()
        #group2_comp = tukey_data.loc[tukey_data.reject == True].groupby('group2').reject.count()
        #tukey_data = pd.concat([group1_comp, group2_comp], axis=1)
        
        #print(tukey_data)
        
        #tukey_data = tukey_data.fillna(0)
        #tukey_data.columns = ['reject1', 'reject2']
        #tukey_data['total_sum'] = tukey_data.reject1 + tukey_data.reject2
        
        df = tukey_data[tukey_data['reject'] == True]
        print(df)

        
        print()
        print()
        print()
        
        # Remove spaces in 'group1' and 'group2' labels
        df['group1'] = df['group1'].str.replace(' ', '')
        df['group2'] = df['group2'].str.replace(' ', '')
  
        # Concatenate 'group1' and 'group2' into a single column
        df['group'] = df['group1'] + ':' + df['group2']

        # Create a bar plot using sns.barplot
        fig, ax = plt.subplots()
        sns.barplot(data=df, x='meandiff', y='group', palette='coolwarm', ax=ax)

        # Set the x-axis and y-axis labels
        ax.set_xlabel('meandiff')
        ax.set_ylabel('group1/group2')

        # Display the plot
        plt.show()


















"""
        if normality == False:
            #Friedman test --> data are not normally distributed
            groups = []
            for i in list(data2.group):
                newi = i[2:] #remove 'gr' from group name take only number of group because friedman test needs only numbers
                #print(newi)
                groups.append(newi)
                
            #print(groups)
                
            genders = []
            for i in list(data2.gender):
                if i == 'M':
                    i = 0
                elif i == 'F':
                    i = 1
                genders.append(i)
            
            res2 = stats.friedmanchisquare(genders, groups, data2[col]) #["TMC"]
            print(res2)
            
            #posthoc test for determining which groups are different
            #data_arr = np.array([genders, groups, list(data2.col)])
            #perform Nemenyi post-hoc test
            #print("which groups are different")
            #print(sp.posthoc_nemenyi_friedman(data_arr.T))
            
            print()
            
        else:
            # Performing two-way ANOVA
            print()
            print(col)
            print(data2)
            data2.reset_index(inplace=True)

            model = ols(
            '{} ~ C(gender) + C(group) +\
            C(gender):C(group)'.format(col), data=data2).fit()
            res = sm.stats.anova_lm(model, typ=2)
            print(res)
        

"""
            
        

        
        #combine three groups into one array
       #print(genders)
        #print(groups)
        #print(list(data2.TMC))
        #data_arr = np.array([genders, groups, list(data2.TMC)])
       # print(data_arr.dtype)
        #data_arr = data_arr.astype(float)
  
   

       
        

        
        
        
        
        ################################################################

#todle je zatim spatne --> dava mi to spatne groups ktere se lisi --> vsude to stejne
            #if p_val_fried < 0.05:
            #posthoc test for determining which groups are different
               # data_arr = np.array([genders, groups, data2[col]])
                #print(data_arr)
            #perform Nemenyi post-hoc test
            #print("which groups are different")
               # print(sp.posthoc_nemenyi_friedman(data_arr.T))
               # print() #jen pro odradkovani
   
        #perform Nemenyi post-hoc test
        #print("which groups are different")
        #print(sp.posthoc_nemenyi_friedman(data_arr.T))
        
        
        
        
        
"""
        --------------------------------------------------------------------------------------------------------------------------------
             jen pro moje zjisteni a data do matlabu
        groups = []
        for i in list(data2.group):
            if i == 'gr1':
                i = 1
            elif i == 'gr2':
                i = 2
            elif i == 'gr3':
                i = 3
            elif i == 'gr4':
                i = 4
            elif i == 'gr5':
                i = 5
            elif i == 'gr6':
                i = 6
            elif i == 'gr7':
                i = 7
            elif i == 'gr8':
                i = 8
            elif i == 'gr9':
                i = 9
            elif i == 'gr10':
                i = 10
            elif i == 'gr11':
                i = 11
            groups.append(i)
        print()
        print("groups")
        print(groups)
            
        
              print("data")
        print(list(data2.gender))
        genders = []
        for i in list(data2.gender):
            if i == 'M':
                i = 0
            elif i == 'F':
                i = 1
            genders.append(i)
        print("genders")
        print(genders)
        --------------------------------------------------------------------------------------------------------------------------------
        
        
        data3 = data[['group','gender',col]]
        print("data3")
        print(data3.gender)

       
        
        # Performing two-way ANOVA
        print(col)
        data2.reset_index(inplace=True)

        model = ols(
        '{} ~ C(group) + C(gender) +\
        C(group):C(gender)'.format(col), data=data3).fit()
        res = sm.stats.anova_lm(model, typ=2)
        print(res)
        
"""

    

