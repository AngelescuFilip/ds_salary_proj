

import pandas as pd 
import numpy as np
import re

df = pd.read_csv('glassdoor_octoparse_v2.csv')

# company name text only
# state field
# age og company
# parsing of job description

# Salary parsing
attributes = ['Revenue', 'Industry', 'Founded', 'Type', 'Size', 'Sector']
for i in attributes:
    df[i] = df[i].apply(lambda x: x.replace(i+'\n', ''))   

df['hourly'] = df['Salary_Estimate'].apply(lambda x: 1 if 'per hour' in x.lower() else 0)
df['employer_provided'] = df['Salary_Estimate'].apply(lambda x: 1 if 'employer provided salary:' in x.lower() else 0)

salary = df['Salary_Estimate'].apply(lambda x: x.replace('(Glassdoor est.)', ''))
minus_Kd = salary.apply(lambda x: x.replace('K', '').replace('$', ''))


min_hr = minus_Kd.apply(lambda x: x.lower().replace('per hour', '').replace('employer provided salary:', ''))   

df['min_salary'] = min_hr.apply(lambda x: x.split(' - ')[0] if '-' in x else x).astype(float)
df['max_salary'] = min_hr.apply(lambda x: x.split(' - ')[1] if '-' in x else x).astype(float)

df['avg_salary'] = (df.min_salary + df.max_salary) / 2

# Company text only
df['Company_Name'] = df['Company_Name'].apply(lambda x: re.sub(r'[0-9.\n]', '', x))

# State field
df['job_state'] = df['Location'].apply(lambda x: x.split(',')[1] if ',' in x else x) 
df.job_state.value_counts()

# Age of company
df['age'] = df['Founded'].apply(lambda x: x if x == 'empty' else 2023 - int(x) )

# Parsing of job description 
df['Description'][0]

# python
df['python_yn'] = df['Description'].apply(lambda x: 1 if 'python' in x.lower() else 0)
df['python_yn'].value_counts()

# spark
df['spark_yn'] = df['Description'].apply(lambda x: 1 if 'spark' in x.lower() else 0)
df['spark_yn'].value_counts()

# aws
df['aws_yn'] = df['Description'].apply(lambda x: 1 if 'aws' in x.lower() else 0)
df['aws_yn'].value_counts()

# excel
df['excel_yn'] = df['Description'].apply(lambda x: 1 if 'excel' in x.lower() else 0)
df['excel_yn'].value_counts()

# sql
df['sql_yn'] = df['Description'].apply(lambda x: 1 if 'sql' in x.lower() else 0)
df['sql_yn'].value_counts()

# tableau
df['tableau_yn'] = df['Description'].apply(lambda x: 1 if 'tableau' in x.lower() else 0)
df['tableau_yn'].value_counts()

# pytorch
df['pytorch_yn'] = df['Description'].apply(lambda x: 1 if 'pytorch' in x.lower() else 0)
df['pytorch_yn'].value_counts()

df.columns
df_out = df.drop(['Unnamed: 0'], axis=1)

df_out.to_csv('glassdoor_salary_data_cleaned.csv', index=False)











