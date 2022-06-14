#%%
##For Exercises 21-25, work with the Nutrition_subset data set. The data set contains the weight in grams along with the amount of saturated fat and the amount of chelesterol for a set of 961 foods. Use either Python or R to solve each problem.
import pandas as pd
import numpy as np

dfNutrition = pd.read_csv("Datasets\\nutrition_subset")

#%%
#Q21 The elements in the data set are fodd items of various sizes, ranging from a teaspoon fo cinnamon to  an entire carrot cake.
#Q21a Sort the data set by the saturated fat (saturated_fat) and produce a listing of the five food items highest in saturated fat.
dfNutrition = dfNutrition.sort_values(by=['saturated_fat'], ascending=False)
dfNutrition.head(5)

#Q21b Comment on the validity of compring food items of different sizes.
# Saturated Fat should be represeneted as a proportion by weight.

#%%
#Q22 Derive a new variable, saturated_fat_per_gram, by dividing the amount of saturated fat by the weight in grams.
dfNutrition['saturated_fat_per_gram'] = dfNutrition['saturated_fat'] / dfNutrition['weight_in_grams']
#Q22a Sort the data set by saturated_fat_per_gram and produce a listing of the five food items hightest in saturated fat per gram.
dfNutrition = dfNutrition.sort_values(by=['saturated_fat_per_gram'], ascending=False)
dfNutrition.head(5)

#Q22b Which food has the mostsaturated fat per gram?
#BUTTER; SALTED & UNSALTED 1 TBSP

#%%
#Q23 Derive a new variable, cholesterol_per_gram.
dfNutrition['cholesterol_per_gram'] = dfNutrition['cholesterol'] / dfNutrition['weight_in_grams']
#Q23a Sort the data set by cholesterol_per_gram and produce a listing of the five food items hightest in cholesterol fat per gram.
dfNutrition = dfNutrition.sort_values(by=['cholesterol_per_gram'], ascending=False)
dfNutrition.head(5)

#Q23b Which food has the cholesterol fat per gram
# EGG; RAW; YOLK 1 YOLK

#%%
#Q24 Standardize the field saturated_fat_per_gram. Produce a listing of all the food items that are outliers at the high end of the scale. How many food items are outliers at the low end of the scale?
dfNutrition['saturated_fat_per_gram_z'] = (dfNutrition['saturated_fat_per_gram'] - dfNutrition['saturated_fat_per_gram'].agg('mean')) / dfNutrition['saturated_fat_per_gram'].agg('std') 
print('High Outliers of saturated_fat_per_gram: ')
print(dfNutrition.query('saturated_fat_per_gram_z > 3')['food item'])
print('\nNumber of low Outliers for saturated_fat_per_gram: ' + str(len(dfNutrition.query('saturated_fat_per_gram_z < -3'))))

#%%
#Q25 Standardize the field cholesterol_fat_per_gram. Produce a listing of all the food items that are outliers at the high end of the scale.
dfNutrition['cholesterol_per_gram_z'] = (dfNutrition['cholesterol_per_gram'] - dfNutrition['cholesterol_per_gram'].agg('mean')) / dfNutrition['cholesterol_per_gram'].agg('std') 
print('High end outliers for cholesterol_fat_per_gram:')
print(dfNutrition.query('cholesterol_per_gram_z > 3')['food item'])

#%%
#For Excercises 26-30, work with the adult_ch3_training data set. The repsone is whether income exceeds $50,000.
dfAdult = pd.read_csv("Datasets\\adult_ch3_training")

#%%
#Q26 Add a record index field to the data set
dfAdult = dfAdult.reset_index()

#%%
#Q27 Determine whether any outliers exist for the education field.
dfAdult['education_z']  = (dfAdult['education'] - dfAdult['education'].agg('mean')) / dfAdult['education'].agg('std')
dfAdult.query('education_z > 3 | education_z < -3')

#%%
#Q28 Do the following for the age field.
#Q28a Standardize the variable.
dfAdult['age_z'] = (dfAdult['age'] - dfAdult['age'].agg('mean')) / dfAdult['age'].agg('std')
#Q28b Identify how many outliers there are and idnetify the most extreme outlier.
print('Outliers for age: ' + str(len(dfAdult.query('age_z > 3 | age_z < -3'))))
print('Most extream outlier for age: ')
dfAdult.sort_values(by=['age_z'], ascending=False).head(1)
#%%
dfAdult.sort_values(by=['age_z'], ascending=False).tail(1)

#%%
#Q29 Derive a flag for capital-gain, called capital-gain-flag, which equals 0 for capital gain equals zero, and 1 otherwise
dfAdult.loc[dfAdult['capital-gain'] == 0, 'capital-gain-flag'] = 0
dfAdult.loc[dfAdult['capital-gain'] != 0, 'capital-gain-flag'] = 1

#%%
#Q
#%%
#Q
#%%
#Q


#%%
#Q
#%%
#Q
#%%
#Q