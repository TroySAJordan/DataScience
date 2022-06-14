#%%
# #For the following exercises, work with the bank_marketing_training data set. Use either Python or R to solve each problem.
import pandas as pd
import numpy as np
df = pd.read_csv(r"C:\Users\troy.jordan\OneDrive - HMG HARDCHROME PTY LTD\Data Science Using Python and R\Datasets\bank_marketing_training")

#%%
#Q11: Derive an index field and add it to the data set
df = df.reset_index()

#%%
#Q12: For the days_since_previous field, change the field value 999 to the appropriate code for missing values.
df['days_since_previous'] = df['days_since_previous'].replace({999: np.NaN})

#%%
#Q13: For the education field, reexpress the field values as the numeric values shown in Table 3.1
df['education_numerical'] =df['education'].replace({'unknown': np.NaN, 'illiterate': 0, 'basic.4y': 4, 'basic.6y': 6, 'basic.9y': 9, 'high.school': 12, 'professional.course': 12, 'university.degree': 16})

#%%
#Q14: Standardize the field age. Print out a list of the frst 10 records, including the variables age and age_z.
df['age_z'] = (df['age'] - df['age'].agg('mean')) / df['age'].agg('std')
df[['age', 'age_z']].head(10)

#%%
#Q15: Obtain a listing of all records that are outliers according to the field age_z. Print out a listing of the 10 largest age_z values.
df.query('age_z > 3 | age_z < -3')

#%%
#Q16: For the job field, combine the jobs with less than 5% of the records into a field called other.
#this gets list of jobs with index True or False showing if < 5%
df1 = pd.DataFrame(df[['job', 'index']].groupby('job').agg('count')/len(df) < 0.05).reset_index()
df1['newjob'] = df1['job']
df1['newjob'] = df1.where(df1['index'] == False, 'other')
#this 
df2 = df1[['job', 'newjob']].set_index('job').to_dict()['newjob']

#this makes df from original df and replaces value based on dictionary
df['job'] = df['job'].replace(df2)

#%%
#Q17: Rename the default predictor to credit_default.
df = df.rename(columns={'default': 'credit_default'})

#%%
#Q18: For the variable month, change the field values to 1-12, but keep the variable as categorical.
df['month'] = df['month'].replace({'jan': 1, 'feb': 2, 'mar': 3, 'apr': 4, 'may': 5, 'jun': 6, 'jul': 7, 'aug': 8, 'sep': 9, 'oct': 10, 'nov': 11, 'dec': 12, })

#%%
#Q19: Do the following for the duration field.
    #a: Standardize the varibale.
    #b: Identify how many outliers there rae and identify the most extreme outlier.
df['duration_z'] = (df['duration'] - df['duration'].agg('mean')) / df['duration'].agg('std')
df[['duration', 'duration_z']].head(10)
df.query('duration_z > 3 | duration_z < -3')

#%%
#Q20: Do the following for the campaign field.
    #a: Standardize the varibale.
    #b: Identify how many outliers there rae and identify the most extreme outlier.
df['campaign_z'] = (df['campaign'] - df['campaign'].agg('mean')) / df['campaign'].agg('std')
df[['campaign', 'campaign_z']].head(10)
df.query('campaign_z > 3 | campaign_z < -3')
