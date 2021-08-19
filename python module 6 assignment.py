# 1
import pandas as pd
cities = pd.read_csv(r'C:\Users\WIN10\Desktop\LEARNING\DS\Python Problem Statements\Indian_cities.csv')
print(cities)

# (a)
# For finding out top 10 states in female to male sex ratio
ratio = (cities.male_graduates/cities.female_graduates)
cities.insert(1,'Ratio',ratio)
cities.nlargest(10,'Ratio')

# (b)
# For finding top 10 cities in total number of graduates
cities.nlargest(10, 'total_graduates')

# (c)
# For printing effective literacy rate
cities.nlargest(10, 'sex_ratio')
cities.nlargest(10, 'total_graduates')
state = cities.state_name
print(state)
cities.insert(1, 'Statename', state)
print(cities)
cities.nlargest(10, ['effective_literacy_rate_total'])

# 2
# (a)
# Constructing Histogram on literates_total
import matplotlib.pyplot as plt
plt.hist(cities['literates_total'],color='red',bins=10)
plt.xlabel('literates_total')
plt.ylabel('frequency')
plt.title('literates_total VS frequency')
# From the above histogram we can tell that it is positively skewed

# (b)
# Constructing scatter plot between male and female graduates
plt.scatter(cities.male_graduates,cities.female_graduates);plt.xlabel('Male Graduates');plt.ylabel('Female Graduates')
# From the graph the direction is positive and strength is moderate
# To calculate the correlation coefficient values 
from scipy.stats import pearsonr as pr
correlation= pr(cities.male_graduates,cities.female_graduates)
print(correlation)
# From the correlation coefficient calculation since r>0.85 the strength is strong

# 3
# (a)
# Constructing Box Plot
plt.boxplot(cities.effective_literacy_rate_total);plt.ylabel("Total effective literacy rate");plt.xlabel("Frequency")

# Detection of outliers from the formula

IQR = cities['effective_literacy_rate_total'].quantile(0.75) - cities['effective_literacy_rate_total'].quantile(0.25)
IQR
ll = cities['effective_literacy_rate_total'].quantile(0.25) - (IQR * 1.5)
ll 
# Values lesser than this are considered as outliers
ul = cities['effective_literacy_rate_total'].quantile(0.75) + (IQR * 1.5)
ul # Values greater than this are considered as outliers
cities.effective_literacy_rate_total.describe() 

# For listing out the outliers we define the user defined function
outlier =[] 
for x in cities.effective_literacy_rate_total: 
    if ((x > ul) or (x < ll)): 
         outlier.append(x) 
print("Outlier in the dataset = ", outlier) 

# To conform whether the outliers is actual outliers or not
llfinal = cities['effective_literacy_rate_total'].quantile(0.25) - (IQR * 3)
llfinal 
# Here the values lesser than this are considered as actual outliers.
# To listout the actual outliers from the dataset we wrote a user defined function.
outlierfinal =[] 
for y in cities.effective_literacy_rate_total: 
    if (y < llfinal): 
         outlierfinal.append(y) 
print("Outlier in the dataset is actual= ", outlierfinal) 

# (b)
# Finding out the null values
cities.isna().sum()
# There are no NA values in the dataset
cities.isnull().sum()
# There are no null values in the dataset.
