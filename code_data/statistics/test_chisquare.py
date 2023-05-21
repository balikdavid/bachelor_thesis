"""
In this code, we first generate a random array of 595 elements using the numpy.random.normal() function.
We then calculate the mean and standard deviation of the array using the numpy.mean() and numpy.std() functions.

Next, we define the z-score intervals as a list of tuples. For each interval, we calculate the expected frequency
by using the scipy.stats.norm.cdf() function to calculate the cumulative distribution function (CDF) for the upper 
and lower bounds of the interval, and then subtracting the two values. We then multiply each expected frequency by 
the total number of observations in the distribution to get the final expected frequencies.

Finally, we print the expected frequencies using the numpy.array() and print() functions. Note that the expected 
frequencies may not be exact due to the use of the empirical rule, but they should be close for a normally distributed dataset.


# Calculate the mean and standard deviation of the array
mean = np.mean(data)
std_dev = np.std(data)

# Define the z-score intervals
intervals = [(mean - 3*std_dev, mean - 2*std_dev),
             (mean - 2*std_dev, mean - std_dev),
             (mean - std_dev, mean),
             (mean, mean + std_dev),
             (mean + std_dev, mean + 2*std_dev),
             (mean + 2*std_dev, mean + 3*std_dev)]

# Calculate the expected frequencies for each interval using the empirical rule
expected_freqs = []
for interval in intervals:
    expected_freqs.append(norm.cdf(interval[1], loc=mean, scale=std_dev) 
                          - norm.cdf(interval[0], loc=mean, scale=std_dev))
expected_freqs = np.array(expected_freqs) * len(data)

print(expected_freqs)
"""

import numpy as np
from scipy.stats import norm
from scipy.stats import chisquare

# Generate a random array with 595 elements
#data = np.random.normal(loc=0, scale=1, size=595)
x =[10, 0, 12, 10, 10, 10, 12, 12, 11, 10, 11, 12, 3, 7, 10, 9, 12, 0, 11, 0, 12, 12, 0, 11, 0, 0, 8, 11, 0, 10, 5, 12, 
    11, 9, 12, 10, 9, 12, 12, 12, 10, 11, 10, 10, 12, 11, 12, 11, 12, 9, 12, 10, 11, 0, 12, 12, 9, 5, 0, 12, 12, 12, 6, 
    11, 10, 11, 12, 10, 10, 8, 12, 11, 10, 11, 11, 9, 9, 12, 11, 12, 11, 12, 0, 12, 6, 10, 12, 11, 11, 12, 11, 10, 11, 10,
    0, 10, 12, 12, 11, 10, 12, 11, 11, 12, 12, 10, 9, 10, 4, 12, 10, 0, 10, 11, 12, 10, 10, 12, 11, 12, 12, 9, 12, 10, 11, 
    12, 10, 10, 11, 11, 12, 10, 9, 11, 12, 10, 11, 10, 9, 12, 11, 12, 12, 12, 9, 11, 10, 9, 11, 11, 11, 12, 12, 10, 11, 0, 
    0, 9, 11, 12, 11, 10, 12, 0, 10, 12, 11, 11, 11, 11, 11, 10, 10, 9, 12, 10, 11, 12, 11, 10, 11, 12, 12, 10, 11, 12, 10, 
    11, 12, 12, 12, 11, 11, 12, 12, 12, 12, 11, 12, 11, 11, 11, 12, 11, 10, 12, 12, 12, 11, 9, 11, 10, 0, 9, 12, 12, 8, 12, 
    12, 0, 12, 12, 11, 12, 12, 10, 0, 11, 11, 11, 11, 12, 11, 11, 11, 12, 11, 10, 12, 11, 12, 12, 11, 10, 12, 9, 12, 12, 6, 12, 
    11, 11, 12, 12, 12, 11, 11, 10, 12, 12, 11, 12, 12, 10, 11, 12, 10, 12, 9, 12, 12, 11, 11, 12, 7, 12, 12, 11, 12, 12, 12, 12, 
    11, 12, 10, 12, 12, 10, 10, 11, 12, 10, 12, 12, 11, 11, 9, 12, 10, 12, 12, 10, 8, 12, 10, 12, 12, 11, 12, 11, 11, 12, 12, 12, 12, 
    12, 12, 11, 11, 12, 9, 10, 11, 12, 12, 10, 11, 12, 12, 12, 11, 12, 12, 12, 12, 11, 10, 10, 10, 12, 10, 11, 10, 10, 11, 10, 12, 12, 10, 
    12, 12, 12, 12, 12, 10, 12, 10, 11, 11, 12, 12, 10, 12, 12, 11, 9, 11, 10, 10, 12, 11, 11, 12, 11, 12, 9, 12, 12, 12, 9, 12, 12, 12,
    12, 10, 11, 12, 12, 10, 11, 12, 11, 0, 11, 12, 12, 11, 12, 12, 11, 12, 12, 11, 11, 10, 6, 8, 12, 12, 11, 11, 12, 11, 10, 10, 12, 10,
    9, 11, 12, 10, 11, 10, 10, 12, 12, 12, 12, 11, 12, 12, 11, 12, 12, 12, 10, 11, 11, 9, 11, 10, 12, 8, 10, 12, 12, 12, 12, 12, 12, 0, 
    12, 11, 11, 12, 12, 12, 12, 12, 9, 12, 12, 11, 12, 12, 12, 11, 10, 11, 11, 11, 12, 11, 9, 12, 11, 9, 10, 11, 10, 12, 11, 12, 12, 12,
    12, 12, 12, 11, 11, 10, 9, 11, 10, 10, 11, 12, 12, 0, 12, 10, 12, 12, 10, 12, 11, 12, 12, 11, 12, 12, 10, 12, 11, 12, 12, 10, 0, 11, 
    11, 12, 11, 11, 10, 12, 12, 11, 10, 11, 11, 12, 10, 12, 10, 9, 11, 10, 9, 12, 12, 12, 11, 8, 11, 11, 12, 11, 12, 12, 11, 11, 11, 12,
    12, 12, 11, 12, 8, 10, 11, 12, 12, 12, 12, 11, 6, 12, 11, 11, 11, 12, 11, 11, 11, 12, 11, 12, 11, 11, 12, 10, 12, 12, 11, 11, 12, 10, 10, 12, 12, 11, 12, 10, 11, 11]




x = sorted(x)
print(x)
sum = 0
for i in x:
    sum += 1

print("sum " + str(sum))
counts = np.bincount(x)
print(counts)
probs = counts / len(x)
print(probs)
print(chisquare(probs))







