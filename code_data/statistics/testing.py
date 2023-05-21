import pandas as pd
from scipy import stats
import helpers as h
import matplotlib.pyplot as plt
import statsmodels.stats.multicomp as mc
import numpy as np
import seaborn as sns
import statsmodels.api as sm
from statsmodels.formula.api import ols
import re
from statsmodels.stats.diagnostic import lilliefors
from scipy.stats import chisquare, norm, chi2
import matlab.engine
import matlab



"""
tento soubor slouzi pouze pro testovani jednotlivych funkci popripade pro zkousku novych veci
   matlab_engine = matlab.engine.start_matlab()

      # Define data
      data = matlab.double([1, 2, 3, 4, 5, 6, 7, 8])

      # Calculate mean and standard deviation of data
      mean_data = matlab_engine.mean(data)
      std_data = matlab_engine.std(data)

      # Define the normcdf function handle in Python
      normcdf_handle = matlab_engine.inline('x,mu,sigma', 'normcdf(x, mu, sigma)', nargout=1)

      # Call chi2gof function
      h, p, stats = matlab_engine.chi2gof(data, 'cdf', (normcdf_handle, mean_data, std_data))

      # Print the results
      print("h: ", h)
      print("p: ", p)
      print("stats: ", stats)

      # Stop MATLAB Engine API for Python
      matlab_engine.quit()
"""



if __name__ == "__main__":
      
      list1 =  [3, 3, 3, 3, 3, 3, 3, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 1, 3, 3, 2, 3, 3, 3, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 2, 3, 3, 3, 2, 3, 3, 3, 3, 3, 2, 3, 2, 2, 3, 3, 2, 2, 3, 2, 3, 3, 3, 3, 2, 3, 3, 3, 3, 3, 3, 2, 3, 3, 3, 3, 2, 3, 3, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 2, 3, 3, 2, 2, 3, 3, 3, 3, 2, 3, 2, 3, 3, 2, 2, 3, 2, 3, 3, 2, 2, 3, 3, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 2, 2, 2, 3, 3, 3, 2, 3, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 3, 3, 3, 2, 3, 3, 2, 3, 3, 3, 3, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 3, 3, 3, 3, 3, 2, 3, 3, 3, 3, 3, 3, 2, 0, 3, 3, 3, 3, 2, 3, 3, 2, 2, 3, 3, 3, 3, 2, 2, 3, 2, 1, 2, 3, 3, 3, 3, 3, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 3, 3, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 3, 3, 3, 2, 3, 2, 3, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 2, 3, 3, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 2, 3, 2, 3, 3, 3, 3, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 3, 3, 3, 3, 3, 3, 2, 3, 3, 3, 3, 2, 2, 3, 3, 3, 3, 3, 3, 2, 3, 3, 3, 3, 3, 3, 3, 2, 3, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 3, 3, 3, 3, 3, 2, 3, 3, 3, 3, 3, 3, 3, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 3, 3, 3, 3, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 3, 2, 3, 3, 3, 3, 3, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 3, 3, 2, 3, 3, 3, 3, 3, 2, 3, 2, 3, 3, 3, 2, 3, 3, 3, 3, 3, 3, 3, 3, 2, 3, 3, 3, 2]
      print(h.chi_square_test_normality(list1))

      
      
      
      
      
      
      # Start MATLAB Engine API for Python
      matlab_engine = matlab.engine.start_matlab()

      # Call the built-in MATLAB function to create a magic square
      magic_square = matlab_engine.magic(4)

      # Print the magic square
      print(magic_square)

      # Stop MATLAB Engine API for Python
      matlab_engine.quit()


      # Start MATLAB Engine API for Python
      matlab_engine = matlab.engine.start_matlab()

      # Define data
      data = matlab.double([1, 1, 1, 1, 2, 2, 3, 3,1, 1, 1, 1, 2, 2, 3, 3,1, 1, 1, 1, 2, 2, 3, 3,1, 1, 1, 1, 2, 2, 3, 3])
      print(matlab_engine.length(data))

      # Calculate mean and standard deviation of data
      mean_data = matlab_engine.mean(data)
      std_data = matlab_engine.std(data)

      # Define the normcdf function handle in Python
      normcdf_handle = matlab_engine.inline('x,mu,sigma', 'normcdf(x, mu, sigma)', nargout=1)

      # Call chi2gof function with normcdf_handle
      h, p, stats = matlab_engine.chi2gof(data, 'expected', [20,8,4])

      # Print the results
      print("h: ", h)
      print("p: ", p)
      print("stats: ", stats)

      # Stop MATLAB Engine API for Python
      matlab_engine.quit()

  

      list1 =  [3, 3, 3, 3, 3, 3, 3, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 1, 3, 3, 2, 3, 3, 3, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 2, 3, 3, 3, 2, 3, 3, 3, 3, 3, 2, 3, 2, 2, 3, 3, 2, 2, 3, 2, 3, 3, 3, 3, 2, 3, 3, 3, 3, 3, 3, 2, 3, 3, 3, 3, 2, 3, 3, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 2, 3, 3, 2, 2, 3, 3, 3, 3, 2, 3, 2, 3, 3, 2, 2, 3, 2, 3, 3, 2, 2, 3, 3, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 2, 2, 2, 3, 3, 3, 2, 3, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 3, 3, 3, 2, 3, 3, 2, 3, 3, 3, 3, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 3, 3, 3, 3, 3, 2, 3, 3, 3, 3, 3, 3, 2, 0, 3, 3, 3, 3, 2, 3, 3, 2, 2, 3, 3, 3, 3, 2, 2, 3, 2, 1, 2, 3, 3, 3, 3, 3, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 3, 3, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 3, 3, 3, 2, 3, 2, 3, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 2, 3, 3, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 2, 3, 2, 3, 3, 3, 3, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 3, 3, 3, 3, 3, 3, 2, 3, 3, 3, 3, 2, 2, 3, 3, 3, 3, 3, 3, 2, 3, 3, 3, 3, 3, 3, 3, 2, 3, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 3, 3, 3, 3, 3, 2, 3, 3, 3, 3, 3, 3, 3, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 3, 3, 3, 3, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 3, 2, 3, 3, 3, 3, 3, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 3, 3, 2, 3, 3, 3, 3, 3, 2, 3, 2, 3, 3, 3, 2, 3, 3, 3, 3, 3, 3, 3, 3, 2, 3, 3, 3, 2]
   
      print("list1")
      print(lilliefors(list1,dist='norm',pvalmethod='table'))
      
      data = [10, 0, 12, 10, 10, 10, 12, 12, 11, 10, 11, 12, 3, 7, 10, 9, 12, 0, 11, 0, 12, 12, 0, 11, 0, 0, 8, 11, 0, 10, 5, 12, 11, 9, 12, 10, 9, 12, 12, 12, 10, 11, 10, 10, 12, 11, 12, 11, 12, 9, 12, 10, 11, 0, 12, 12, 9, 5, 0, 12, 12, 12, 6, 11, 10, 11, 12, 10, 10, 8, 12, 11, 10, 11, 11, 9, 9, 12, 11, 12, 11, 12, 0, 12, 6, 10, 12, 11, 11, 12, 11, 10, 11, 10, 0, 10, 12, 12, 11, 10, 12, 11, 11, 12, 12, 10, 9, 10, 4, 12, 10, 0, 10, 11, 12, 10, 10, 12, 11, 12, 12, 9, 12, 10, 11, 12, 10, 10, 11, 11, 12, 10, 9, 11, 12, 10, 11, 10, 9, 12, 11, 12, 12, 12, 9, 11, 10, 9, 11, 11, 11, 12, 12, 10, 11, 0, 0, 9, 11, 12, 11, 10, 12, 0, 10, 12, 11, 11, 11, 11, 11, 10, 10, 9, 12, 10, 11, 12, 11, 10, 11, 12, 12, 10, 11, 12, 10, 11, 12, 12, 12, 11, 11, 12, 12, 12, 12, 11, 12, 11, 11, 11, 12, 11, 10, 12, 12, 12, 11, 9, 11, 10, 0, 9, 12, 12, 8, 12, 12, 0, 12, 12, 11, 12, 12, 10, 0, 11, 11, 11, 11, 12, 11, 11, 11, 12, 11, 10, 12, 11, 12, 12, 11, 10, 12, 9, 12, 12, 6, 12, 11, 11, 12, 12, 12, 11, 11, 10, 12, 12, 11, 12, 12, 10, 11, 12, 10, 12, 9, 12, 12, 11, 11, 12, 7, 12, 12, 11, 12, 12, 12, 12, 11, 12, 10, 12, 12, 10, 10, 11, 12, 10, 12, 12, 11, 11, 9, 12, 10, 12, 12, 10, 8, 12, 10, 12, 12, 11, 12, 11, 11, 12, 12, 12, 12, 12, 12, 11, 11, 12, 9, 10, 11, 12, 12, 10, 11, 12, 12, 12, 11, 12, 12, 12, 12, 11, 10, 10, 10, 12, 10, 11, 10, 10, 11, 10, 12, 12, 10, 12, 12, 12, 12, 12, 10, 12, 10, 11, 11, 12, 12, 10, 12, 12, 11, 9, 11, 10, 10, 12, 11, 11, 12, 11, 12, 9, 12, 12, 12, 9, 12, 12, 12, 12, 10, 11, 12, 12, 10, 11, 12, 11, 0, 11, 12, 12, 11, 12, 12, 11, 12, 12, 11, 11, 10, 6, 8, 12, 12, 11, 11, 12, 11, 10, 10, 12, 10, 9, 11, 12, 10, 11, 10, 10, 12, 12, 12, 12, 11, 12, 12, 11, 12, 12, 12, 10, 11, 11, 9, 11, 10, 12, 8, 10, 12, 12, 12, 12, 12, 12, 0, 12, 11, 11, 12, 12, 12, 12, 12, 9, 12, 12, 11, 12, 12, 12, 11, 10, 11, 11, 11, 12, 11, 9, 12, 11, 9, 10, 11, 10, 12, 11, 12, 12, 12, 12, 12, 12, 11, 11, 10, 9, 11, 10, 10, 11, 12, 12, 0, 12, 10, 12, 12, 10, 12, 11, 12, 12, 11, 12, 12, 10, 12, 11, 12, 12, 10, 0, 11, 11, 12, 11, 11, 10, 12, 12, 11, 10, 11, 11, 12, 10, 12, 10, 9, 11, 10, 9, 12, 12, 12, 11, 8, 11, 11, 12, 11, 12, 12, 11, 11, 11, 12, 12, 12, 11, 12, 8, 10, 11, 12, 12, 12, 12, 11, 6, 12, 11, 11, 11, 12, 11, 11, 11, 12, 11, 12, 11, 11, 12, 10, 12, 12, 11, 11, 12, 10, 10, 12, 12, 11, 12, 10, 11, 11]
      print("list5")
      #print(lilliefors(list5,dist='norm',pvalmethod='table')) #matlab approved --> same results
      
      
      #chisquare test
     # data = [1, 2, 3, 4, 5]
     # print(h.chi_square_test_normality2(data))
     # Input data
      #data = [10, 0, 12, 10, 10, 10, 12, 12]

      # calculate mean and standard deviation
      x = [10, 0, 12, 10, 10, 10, 12, 12, 11, 10, 11, 12, 3, 7, 10, 9, 12, 0, 11, 0, 12, 12, 0, 11, 0, 0, 8, 11, 0, 10, 5, 12, 11, 9, 12, 10, 9, 12, 12, 12, 10, 11, 10, 10, 12, 11, 12, 11, 12, 9, 12, 10, 11, 0, 12, 12, 9, 5, 0, 12, 12, 12, 6, 11, 10, 11, 12, 10, 10, 8, 12, 11, 10, 11, 11, 9, 9, 12, 11, 12, 11, 12, 0, 12, 6, 10, 12, 11, 11, 12, 11, 10, 11, 10, 0, 10, 12, 12, 11, 10, 12, 11, 11, 12, 12, 10, 9, 10, 4, 12, 10, 0, 10, 11, 12, 10, 10, 12, 11, 12, 12, 9, 12, 10, 11, 12, 10, 10, 11, 11, 12, 10, 9, 11, 12, 10, 11, 10, 9, 12, 11, 12, 12, 12, 9, 11, 10, 9, 11, 11, 11, 12, 12, 10, 11, 0, 0, 9, 11, 12, 11, 10, 12, 0, 10, 12, 11, 11, 11, 11, 11, 10, 10, 9, 12, 10, 11, 12, 11, 10, 11, 12, 12, 10, 11, 12, 10, 11, 12, 12, 12, 11, 11, 12, 12, 12, 12, 11, 12, 11, 11, 11, 12, 11, 10, 12, 12, 12, 11, 9, 11, 10, 0, 9, 12, 12, 8, 12, 12, 0, 12, 12, 11, 12, 12, 10, 0, 11, 11, 11, 11, 12, 11, 11, 11, 12, 11, 10, 12, 11, 12, 12, 11, 10, 12, 9, 12, 12, 6, 12, 11, 11, 12, 12, 12, 11, 11, 10, 12, 12, 11, 12, 12, 10, 11, 12, 10, 12, 9, 12, 12, 11, 11, 12, 7, 12, 12, 11, 12, 12, 12, 12, 11, 12, 10, 12, 12, 10, 10, 11, 12, 10, 12, 12, 11, 11, 9, 12, 10, 12, 12, 10, 8, 12, 10, 12, 12, 11, 12, 11, 11, 12, 12, 12, 12, 12, 12, 11, 11, 12, 9, 10, 11, 12, 12, 10, 11, 12, 12, 12, 11, 12, 12, 12, 12, 11, 10, 10, 10, 12, 10, 11, 10, 10, 11, 10, 12, 12, 10, 12, 12, 12, 12, 12, 10, 12, 10, 11, 11, 12, 12, 10, 12, 12, 11, 9, 11, 10, 10, 12, 11, 11, 12, 11, 12, 9, 12, 12, 12, 9, 12, 12, 12, 12, 10, 11, 12, 12, 10, 11, 12, 11, 0, 11, 12, 12, 11, 12, 12, 11, 12, 12, 11, 11, 10, 6, 8, 12, 12, 11, 11, 12, 11, 10, 10, 12, 10, 9, 11, 12, 10, 11, 10, 10, 12, 12, 12, 12, 11, 12, 12, 11, 12, 12, 12, 10, 11, 11, 9, 11, 10, 12, 8, 10, 12, 12, 12, 12, 12, 12, 0, 12, 11, 11, 12, 12, 12, 12, 12, 9, 12, 12, 11, 12, 12, 12, 11, 10, 11, 11, 11, 12, 11, 9, 12, 11, 9, 10, 11, 10, 12, 11, 12, 12, 12, 12, 12, 12, 11, 11, 10, 9, 11, 10, 10, 11, 12, 12, 0, 12, 10, 12, 12, 10, 12, 11, 12, 12, 11, 12, 12, 10, 12, 11, 12, 12, 10, 0, 11, 11, 12, 11, 11, 10, 12, 12, 11, 10, 11, 11, 12, 10, 12, 10, 9, 11, 10, 9, 12, 12, 12, 11, 8, 11, 11, 12, 11, 12, 12, 11, 11, 11, 12, 12, 12, 11, 12, 8, 10, 11, 12, 12, 12, 12, 11, 6, 12, 11, 11, 11, 12, 11, 11, 11, 12, 11, 12, 11, 11, 12, 10, 12, 12, 11, 11, 12, 10, 10, 12, 12, 11, 12, 10, 11, 11];

      mu, sigma = np.mean(data), np.std(data)

      # calculate expected frequencies for normal distribution
      expected = np.array([np.mean(data)] * len(data))

      #expected += 0.01  # add a small constant to each expected frequency
      
      
      print("expected")
      print(expected)
      print("expected len " + str(len(expected)))
      

      # perform chi-squared test of goodness of fit
      chi_squared_statistic, p_value = chisquare(data, expected)

      print("Chi-squared statistic:", chi_squared_statistic)
      print("P-value:", p_value)
      print("")
      
      sample = np.array([1.2, 3.4, 5.6, 7.8, 9.0])
      mu, sigma = norm.fit(sample)
      n_bins = len(sample)
      bin_edges = np.linspace(sample.min(), sample.max(), n_bins+1)
      expected_freq = np.diff(norm.cdf(bin_edges, mu, sigma)) * len(sample)
      observed_freq, _ = np.histogram(sample, bins=bin_edges)
      statistic, p_value = chisquare(observed_freq, expected_freq)
      print("Chi-squared statistic:", statistic)
      print("P-value:", p_value)

    
      
      
      


    

  
      """
  
  
  
      df_list = h.get_multiple_excel_in_df_list()
      suspicious_columns = ['subtest 1','subtest 2','subtest 3','subtest 4',
                          'subtest 5', 'subtest 6', 'subtest 7','subtest 8',
                          'test 1', 'test 2', 'test 3', 'test 4', 'TMC'
                          ]
    
      print(df_list[0].index)
  

   # print(np.median(data[0]))
    #plt.boxplot(data)
  #  plt.show()
    
    #print(stats.f_oneway(*data))
    #df_list[0] = df_list[0].assign(group = 1)
    #print(df_list[0])
    
      for i in range(len(df_list)):
            df_list[i] = df_list[i].assign(group = 'gr'+str(i+1))
        #print(df_list[i][[' TMC','group']])
        #res = pd.concat([df_list[i]],ignore_index=True, names=[' TMC','group'])
    
      data = pd.concat([df for df in df_list],ignore_index=True)
      data = data[['TMC','group']]
      print("data")
      print(data)
      formula = "TMC ~ C(group)"

      model = ols(formula, data).fit()
      anova_table = sm.stats.anova_lm(model, typ=1)
      print(anova_table)
      
      mc = mc.MultiComparison(data['TMC'], data['group'])
      posthoc_res = mc.tukeyhsd()
      posthoc_df = pd.DataFrame(data=posthoc_res._results_table.data[1:], columns=posthoc_res._results_table.data[0])
      print(posthoc_df)
      # Plot the graph
      sns.pointplot(x='group', y='TMC', data=data, ci='sd')
      #sns.pointplot(x='group2', y='mean', data=posthoc_df, color='black', markers='_', scale=1.5, errwidth=1.5, capsize=0.1)

      # Add significance bars
      sig_bars = posthoc_df[posthoc_df['p-adj'] < 0.05]
      for i, row in sig_bars.iterrows():
            plt.plot([row['group1'], row['group2']], [max(data['TMC']) + 0.5, max(data['TMC']) + 0.5], linewidth=1.5, color='black')
            #plt.text((row['group1']+int(row['group2']))/2, max(data['TMC']) + 0.7, '*', ha='center', va='center', fontsize=18)
            
      #plt.show()
      
    
    
    
    
    
    
    
    
    
    
    
    

      data1 = [0.54,1.83,-2.26,0.86,0.32,-1.31,-0.43,0.34,3.58,2.77]
    data3 = []
    for i in data1:
      data3.append(i+1)
      
    print(data3)
    data2 = [100.54,101.83,97.74,100.86,100.32,98.69,99.57,100.34,103.58,102.77]


    stat,p = stats.kstest(data1, "norm")#kstest(data_ind,"norm") #lilieforce testnormaltest
    print(stat,p)
    stat,p = stats.kstest([100.54,101.83,97.74,100.86,100.32,98.69,99.57,100.34,103.58,102.77],"norm")#kstest(data_ind,"norm") #lilieforce testnormaltest
    print(stat,p)
    stat,p = stats.kstest(data3, "norm")#kstest(data_ind,"norm") #lilieforce testnormaltest
    print(stat,p)
"""
    
    
    
    
    
"""
        #data for matlab
    
    data = h.get_column_data(df_list,'TMC')
    data_str = str(data)
    data_str = re.sub(r'\)', '\n', data_str)
    data_str = data_str.replace('(', '').replace(')', '')
    data_str = data_str.replace('array', 'array=').replace(')', '')

    
    print(data_str)
    
    array1=[64, 48, 59, 40, 56, 45, 49, 47, 60, 48, 62, 47, 61, 46, 53, 42, 67,
       63, 66, 60, 63, 52, 27, 66, 35, 45, 32, 51, 42, 55, 59]
    array2=[38, 66, 35, 53, 34, 40, 44, 51, 52, 44, 46, 60, 45, 38, 57, 47, 37,
          46, 62, 39, 54, 50, 56, 60, 43, 45, 49, 53, 56, 54, 40, 33, 66, 51,
          47, 48, 57, 54, 53, 56, 58, 48, 53, 64, 20]
    array3=[48, 56, 47, 51, 48, 34, 35, 51, 50, 44, 44, 33, 30, 51, 44, 40, 57,
          57, 60, 36, 48, 48, 46, 30, 38, 55, 58, 56, 49, 62, 55, 41, 32, 45,
          41, 44, 51, 44, 62, 43, 42, 53, 40, 49, 47, 42, 58, 48, 37, 55, 52,
          61, 58, 54, 58, 46, 39, 59, 46, 48, 46]
    array4=[39, 54, 56, 48, 40, 52, 58, 38, 39, 48, 48, 20, 58, 42, 28, 50, 60,
          42, 45, 40, 40, 48, 30, 39, 61, 51, 63, 64, 59, 49, 43, 45, 47, 52,
          33, 47, 48, 50, 57, 61, 55, 36, 52, 39, 63, 57, 57, 53, 64, 56, 50,
          44]
    array5=[47, 63, 61, 51, 58, 56, 53, 51, 66, 49, 53, 39, 46, 32, 44, 58, 49,
          58, 48, 40, 57, 42, 45, 42, 30, 33, 54, 47, 44, 26, 41, 24, 23, 39,
          48, 35, 48, 40, 51, 65, 59, 53, 51, 64, 49, 49, 50, 55, 32, 52, 49,
          53, 68, 56, 56, 59, 67]
    array6=[49, 46, 58, 51, 61, 43, 49, 33, 51, 47, 37, 50, 51, 43, 68, 47, 33,
          39, 45, 47, 52, 35, 50, 50, 56, 33, 33, 45, 47, 45, 62, 43, 47, 59,
          51, 45, 49, 57, 43, 61, 49, 44, 57, 53, 48, 55, 42, 46, 56, 65, 40,
          48, 57, 30, 55, 59, 48, 50, 61, 40, 42, 56, 50, 60]
    array7=[20, 44, 65, 39, 66, 63, 60, 55, 33, 55, 46, 51, 44, 56, 33, 46, 50,
          47, 49, 37, 50, 61, 51, 51, 55, 49, 46, 42, 31, 28, 51, 44, 50, 57,
          37, 34, 20, 29, 49, 40, 47, 42, 50, 35, 50, 38, 57, 52, 50, 67, 59,
          44, 35, 41, 36, 43, 47, 31, 38, 45, 55, 39, 20]
    array8=[43, 43, 35, 53, 32, 60, 44, 42, 45, 56, 62, 47, 32, 44, 20, 40, 37,
          47, 56, 40, 32, 45, 46, 41, 41, 43, 55, 52, 52, 63, 43, 48, 39, 34,
          34, 55, 67, 48, 41, 48, 37, 44, 39, 64, 34, 40, 53, 43, 28, 58, 38,
          40, 57, 47, 43, 54, 35, 27, 48, 39, 53, 46, 61, 43, 61, 47, 41, 67,
          61, 48, 31, 20, 28]
    array9=[45, 35, 43, 54, 42, 48, 35, 50, 45, 68, 43, 65, 46, 34, 23, 39, 33,
          25, 38, 38, 29, 35, 34, 20, 35, 53, 29, 46, 43, 37, 56, 33, 21, 38,
          47, 53, 49, 53, 24, 49, 62, 44, 48, 44, 45, 37, 26, 33, 32, 37, 33]
    array10=[40, 40, 35, 37, 48, 76, 51, 53, 50, 32, 39, 47, 52, 44, 37, 35, 39,
          36, 36, 45, 37, 28, 20, 33, 40, 38, 32, 34, 54, 58, 48, 49, 46, 40,
          49, 30, 33, 58, 29, 41, 44, 50, 71, 43, 44, 57, 38, 40, 43, 38, 40,
          36, 33, 31]
    array11=[48, 44, 56, 55, 52, 36, 52, 47, 58, 52, 52, 50, 39, 41, 41, 49, 30,
          31, 48, 57, 65, 47, 42, 53, 33, 28, 46, 36, 46, 47, 51, 65, 43, 35,
          20, 48, 31, 48, 40, 43, 21, 50, 39, 38, 23]

    print(len(array1))
    print(len(array2))
    print(len(array3))
    print(len(array4))
    print(len(array5))
    print(len(array6))
    print(len(array7))
    print(len(array8))
    print(len(array9))
    print(len(array10))
    print(len(array11))
    
        
    # Example data
    diameters = [1, 2, 3, 4, 5]
    interval_lower = [0.9, 1.5, 2.2, 3.6, 4.3]
    interval_upper = [1.1, 2.0, 3.1, 4.5, 5.1]

    # Plot interval ranges
    plt.plot(diameters, interval_lower, color='blue', linestyle='--', label='Interval Lower')
    plt.plot(diameters, interval_upper, color='red', linestyle='--', label='Interval Upper')

    # Plot data points
    plt.scatter(diameters, interval_lower, color='blue', label='Data Point')
    plt.scatter(diameters, interval_upper, color='red', label='Data Point')

    # Add labels and legend
    plt.xlabel('Diameter')
    plt.ylabel('Interval Range')
    plt.legend()

    # Show plot
    plt.show()
    
"""