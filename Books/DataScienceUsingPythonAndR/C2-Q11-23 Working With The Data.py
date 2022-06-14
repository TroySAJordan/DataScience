#Q11: Download the program and open the comiler. What is contained in the bottom-right window? The left (for Python) or top-left (for R)?
# I am not using Spyder/R

#Q12: Type a comment stating that you are working on Chapter 2 Excecises.
# I am working on Chapter 2 Excecises!

#Q13: Locate the "RUN" button and note whether there is a keyboard shortcut.
# VS Code F5.

#Q14: Execute the comment from the previous exercise. What is the output? Explain your anser.
# No output, no comments produce any output

#Q15: Import the following packages:
#Q15 A: For Python, import the pandas and numpy packages. Rename the pandas package "pd" and rename the numpy package "np"
# %%
import pandas as pd
import numpy as np
#Q15 B: For R, import the ggplot 2 package. Make sure you both install and open the package.
# I am only using Python!

# %%
#Q16: Import the bank_marketing_training data set and name it bank_train.
bank_train = pd.read_csv(r'\\HMGFS01\user files\Troy Jordan\Personal\Data Science Using Python and R\Datasets\bank_marketing_training')

# %%
#Q17: Create a contingency table of the variables response and previous_outcome from the bank_train data set. Do not save the output from the code.
pd.crosstab(bank_train['previous_outcome'], bank_train['response'])

# %%
#Q18: Rerun the code from the previous exercise, this time saving the output as crosstab_01 (fro Python code) or t1 (for R code).
crosstab_01 = pd.crosstab(bank_train['previous_outcome'], bank_train['response'])

# %%
#Q19: After savin the output in the prevoius exercise, display the output using hte name of the saved output.
crosstab_01

# %%
#Q20: Save the contingency table under a different name. This time, use your last name and favourite number as the name; for example larose42.
jordan7 = crosstab_01

# %%
#Q21: Save the first nine record of the bank_train data set as their own data frame
bank_train_first9 = bank_train.iloc[:9]

# %%
#Q22: Save the age and marital records of the bank_train data set as their own data frame.
bank_train_age_marital = bank_train[['age', 'marital']]

# %%
#Q23: Save the first three records of the ag and marital variables as their own data frame.
bank_train_age_marital_first3 = bank_train_age_marital.iloc[:3]
