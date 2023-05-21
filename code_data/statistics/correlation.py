import pandas as pd
from scipy import stats
import helpers as h
import matplotlib.pyplot as plt
import statsmodels.stats.multicomp as mc
import numpy as np
import seaborn as sns
#from statsmodels.stats.diagnostic import lilliefors
from scipy.stats import spearmanr



def print_graph(corr_matrix, test):
    fig = plt.figure()
    ax = fig.add_subplot(111)
    cax = ax.matshow(corr_matrix,cmap='coolwarm', vmin=-1, vmax=1,)
    
    ticks = np.arange(0,len(test.columns),1)
    ax.set_xticks(ticks)
    #plt.xticks(rotation=90)
    ax.set_yticks(ticks)
    ax.set_xticklabels(test.columns)
    ax.set_yticklabels(test.columns)
    cbar = plt.colorbar(cax)
    ax.set_xlabel("Rozsah testů přislušného subtestu")
    ax.set_ylabel("Rozsah testů přislušného subtestu")

    plt.show()
    
def print_graphs(corr_matrices, tests):
    fig, axes = plt.subplots(nrows=2, ncols=4, figsize=(16, 8))
    
    for i, ax in enumerate(axes.flat):
        corr_matrix = corr_matrices[i]
        test = tests[i]
        cax = ax.matshow(corr_matrix, cmap='coolwarm', vmin=-1, vmax=1)
        ticks = np.arange(0, len(test.columns), 1)
        ax.set_xticks(ticks)
        ax.set_yticks(ticks)
        ax.set_xticklabels(test.columns, rotation=90)
        ax.set_yticklabels(test.columns)
        ax.set_title(f'subtest{i+1}')
        cbar = plt.colorbar(cax, ax=ax)
        ax.set_xlabel("Rozsah testů přislušného subtestu")
        ax.set_ylabel("Rozsah testů přislušného subtestu")
        
    plt.tight_layout()
    plt.show()
    
def print_pvalues(pval):
    # create a mask to only display values greater than 0.05
    pval = np.array(pval)
    mask = pval <= 0.05
    print(mask)
    print(pval)

    ax = sns.heatmap(pval, cmap="YlGnBu", annot=True, fmt=".2f") #, mask=mask

    # set axis labels and title
    ax.set_xlabel("Columns")
    ax.set_ylabel("Rows")
    ax.set_title("P-value Heatmap")

    # display the plot
    plt.show()

if __name__ == "__main__":
    df_list = h.get_multiple_excel_in_df_list()
   # print(df_list)
    #concatenate all dataframes from df_list into one big_df
    big_df = pd.concat(df_list)
    #print(big_df[:6:59])
    #print(big_df.iloc[:,40:47])
    subtest1 = big_df.iloc[:,6:13]
    #print(list(subtest1[1]))
    
    subtest2 = big_df.iloc[:,13:21]
   # print(subtest2)
    
    subtest3 = big_df.iloc[:,21:26]
   # print(subtest3)
    
    subtest4 = big_df.iloc[:,26:33]
   # print(subtest4)
    
    subtest5 = big_df.iloc[:,33:42]
    #print(subtest5)
    
    subtest6 = big_df.iloc[:,42:47]
    print(list(subtest6[37]))
    
    
    
    subtest7 = big_df.iloc[:,47:54]
   # print(subtest7)
    
    subtest8 = big_df.iloc[:,54:59]
   # print(subtest8)
   
   
    corr_matrixes = []
    subtests = [subtest1, subtest2, subtest3, subtest4, subtest5, subtest6, subtest7, subtest8]
    for i in range(0,8):
        subtest_i = "subtest"+str(i+1)
       # print()
       # print(subtest_i)
        #are data normally distributed?
        norm_distr , p = h.are_normally_distributed(subtests[i]) #0.0009999999999998899
        print("Are data normally distributed? ", norm_distr ,p)
        #data not normally distributed --> use spearman correlation
        if norm_distr == False:
            #print("subtest[i]")
            print(subtests[i])
            corr_matrix = subtests[i].corr(method='spearman')
            rho, pval = spearmanr(subtests[i])
            corr_matrixes.append(corr_matrix)
            print(corr_matrix)
            #print("pval: ", pval)
            count = 0
            for row in pval:
                for value in row:
                    if value > 0.05:
                        count += 1
           # print("count")    
           # print(count)
        else:
            corr_matrix = subtests[i].corr(method='pearson')
            corr_matrixes.append(corr_matrix)
            print(corr_matrix)
        print_graph(corr_matrix, subtests[i])
        #print_pvalues(pval)
        
   # print_graphs(corr_matrixes, subtests)
    

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    """
    
    print("spearman mezi raw prislusnymi pro subtest1")
    
    corr_matrix = subtest1.corr(method='spearman')
  
    print("pearson mezi raw prislusnymi pro subtest1")
    corr_matrix = subtest1.corr(method='pearson')
    print(corr_matrix)
    print()
   # print_graph(corr_matrix, subtest1)
   """
   
    """
    
    ////////////////////////////////////////////////////////////////////////
    test of normality only:
    x = big_df.iloc[:,6]
    y = big_df.iloc[:,7]
    print(list(x))
    print(list(y))
    print(lilliefors(x,dist='norm',pvalmethod='table'))
    [ks_x,p_x] = lilliefors(x,dist='norm',pvalmethod='table')
    print(ks_x)
    print(p_x)
    [ks_y,p_y] = lilliefors(y,dist='norm',pvalmethod='table')
    print(ks_y)
    print(p_y)
    
    print("spearman mezi raw 1 a 2")
    print(stats.spearmanr(x,y))
    
    print("pearson mezi raw 1 a 2")
    print(stats.pearsonr(x,y))
    
   //////////////////////////////////////////////////////////////////////// 
    
   
   
   
    print()
    print("try")
    data = [['CDU', 0.415, 57], ['SPD', 0.257, 26], ['Others', 0.328, 40]] 
    df = pd.DataFrame(data, columns = ['Varname', 'prob_dist', 'observed_freq']) 
    df['expected_freq'] = df['observed_freq'].sum() * df['prob_dist']
    print(df)
   """


"""

    df_list = h.get_multiple_excel_in_df_list()
    #concatenate all dataframes from df_list into one bid_df
    big_df = pd.concat(df_list)
    print(big_df.iloc[:,6:13])
    
    subtest1 = big_df.iloc[:,6:13]
    corr_matrix = subtest1.corr(method='spearman')
    print(corr_matrix)
    fig = plt.figure()
    ax = fig.add_subplot(111)
    cax = ax.matshow(corr_matrix,cmap='coolwarm', vmin=-1, vmax=1)
    fig.colorbar(cax)
    ticks = np.arange(0,len(subtest1.columns),1)
    ax.set_xticks(ticks)
    #plt.xticks(rotation=90)
    ax.set_yticks(ticks)
    ax.set_xticklabels(subtest1.columns)
    ax.set_yticklabels(subtest1.columns)
    plt.show()
"""
    
    
    

       






























































"""
import pandas as pd

# create a sample dataframe with test scores for two students
data = {'test1': [80, 90], 'test2': [85, 95], 'test3': [90, 85]}
df = pd.DataFrame(data, index=['student1', 'student2'])
print(df)

# calculate the correlation matrix
corr_matrix = df.corr()

# print the correlation matrix
print(corr_matrix)

Korelační matice ukazuje korelační koeficienty mezi jednotlivými dvojicemi testů. V tomto případě jsou všechny hodnoty na diagonále 1,0, 
což dává smysl, protože test je vždy dokonale korelován sám se sebou.

Hodnoty mimo diagonálu ukazují korelaci mezi dvojicemi testů. Protože hodnoty pro test1 a test2 jsou obě 1,0, 
znamená to, že tyto dva testy mají dokonalou pozitivní korelaci, tj. pokud žák dosáhne dobrých výsledků v testu1, p
ravděpodobně dosáhne dobrých výsledků i v testu2. Totéž platí pro test2 a test1.

Na druhé straně hodnoty pro test1 a test3 i test3 a test1 jsou obě -1,0, což znamená, že tyto dva testy mají dokonalou negativní korelaci. 
To znamená, že pokud žák dosáhne dobrých výsledků v testu1, pravděpodobně dosáhne špatných výsledků v testu3 a naopak.

Podobně hodnoty pro test2 a test3 i pro test3 a test2 jsou obě -1,0, což znamená, že mezi těmito dvěma testy je dokonalá záporná korelace. 
To znamená, že pokud student dosáhne dobrých výsledků v testu2, pravděpodobně dosáhne špatných výsledků v testu3 a naopak.

Celkově korelační matice naznačuje, že test1 a test2 jsou vzájemně vysoce korelované, zatímco test1 a test3, stejně jako test2 a test3, 
jsou korelovány negativně. Bez dalších souvislostí o testech a žácích, kteří je skládali, je však obtížné vyvodit z těchto výsledků nějaké konkrétní závěry.
"""