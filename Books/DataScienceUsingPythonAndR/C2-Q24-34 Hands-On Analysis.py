# %%
#Q24: Import the adult_ch3_training data set using hte "Heading: Yes" setting. Rename the data set adult once it is imported.
import pandas as pd
import numpy as py
adult = pd.read_csv(r'C:\Users\troy.jordan\OneDrive - HMG HARDCHROME PTY LTD\Data Science Using Python and R\Datasets\adult_ch3_training', header=0)


# %%
#Q25: Write a comment explaining the change in the data set name
# I have named this data frame adult

# %%
#Q26: Import the following packages:
#Q26A: For Python, import he DecisionTreeClassifier command from the sklearn.tree package.
#Q26B: For R, import the rpart package. Make sure you both install and open the package.
from sklearn.tree import DecisionTreeClassifier


# %%
#Q27: Create a contingency table of workclass and sex. Save the output as table01.
table01 = pd.crosstab(adult['workclass'], adult['sex'])
table01

# %%
#Q28: Create a contingency table of sex and marital status. Save the output as table02.
table02 = pd.crosstab(adult['marital-status'], adult['sex'])
table02

# %%
#Q29: Display the sex and workclass values of the person in the first record. 
# What cell of table01 do they belong to? The one with 444 records.
# How many other records in the data set have the same sex and workclass values? 991
adult[['sex', 'workclass']].iloc[:1]
len(adult[(adult['sex'] == 'Male') & (adult['workclass'] == 'Self-emp-not-inc')]['sex'])
#992 records which are Male and Self-emp-not-inc, making it 991 other records.

# %%
#Q30: Display the sex and marital status values of the people in records 6-10. 
# Which cells of table02 do they belong to? Cells with values 6010 & 795
# How many other records in the data set have the same combination of sex and marital status? 6805
adult[['sex', 'marital-status']].iloc[6:11]
len(adult[(adult['sex'] == 'Male') & ((adult['marital-status'] == 'Married-civ-spouse') | (adult['marital-status'] == 'Divorced'))]['sex'])

# %%
#Q31: Create a new data set that has only records whose maritial status is "Married-civ-spouse" and name the data set adultMarried.
adultMarried = adult[adult['marital-status'] == 'Married-civ-spouse']

# %%
#Q32: Recreate the contingency table of sex and workclass using adultMarried data set. 
# What differences do you notice between the sexes? There are more working Married Males than Females. 
table01Married = pd.crosstab(adultMarried['workclass'], adultMarried['sex'])

# %%
#Q33: Create a new data set that has only records whose age value is greater than 40. Name the new data set adultOver40.
adultOver40 = adult[adult['age'] > 40]


# %%
#Q34: Recreate the contingency tabel of sex and marital status using the adultOver40 data set.
# What differecnes do you notice? 
#  There is a large number & percentage of Married-civ-spouse which are Males.
#  There is a large number & percentage of Widowed which are Female.
table02Over40 = pd.crosstab(adultOver40['marital-status'], adultOver40['sex'])

# %%
