import pandas as pd
from scipy import stats
import helpers as h
import matplotlib.pyplot as plt
import statsmodels.stats.multicomp as mc
import numpy as np
import seaborn as sns








if __name__ == "__main__":
    
    df_list = h.get_multiple_excel_in_df_list()
    data = h.get_column_data(df_list,'TMC')
    flat_list = [item for sublist in data for item in sublist]
    #vypocet distribucni funkce
    counts, bin_edges = np.histogram(flat_list, bins=20, density=True)
    cum_counts = np.cumsum(counts)
    total_counts = cum_counts[-1]
    cdf = cum_counts / total_counts
    
    # Plot the distribution function
    sns.set()
    fig, ax = plt.subplots()
    sns.lineplot(x=bin_edges[1:], y=cdf, drawstyle='steps-post',label='CDF of column TMC', ax=ax)
    ax.set_xlabel('Data celkového motorického koeficeintu')
    ax.set_ylabel('F(x)')
    ax.set_title('Empirical CDF')
    
    
    # Calculate mean and standard deviation of your data
    mean = np.mean(flat_list)
    std = np.std(flat_list)

    # Generate CDF values for a normal distribution with the same mean and std as your data
    x = np.linspace(min(flat_list), max(flat_list), 100)
    normal_cdf = stats.norm.cdf(x, loc=mean, scale=std)

    # Add the normal CDF to the existing graph
    sns.lineplot(x=x, y=normal_cdf, color='red', label='CDF of Normal distribution', ax=ax)
    ax.legend()
    plt.show()

