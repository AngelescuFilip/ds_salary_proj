
import pandas as pd 
import numpy as np

df = pd.read_csv('glassdoor_octoparse.csv')
# df length is 772 rows

df = df.drop_duplicates()
# df length becomes 153
# glassdoor starts cycling results after a while. From the 7th page or so, most of the 1st page results seem to be shown on every page onwards.
# you can use this url for manual testing = https://www.glassdoor.com/Job/data-scientist-jobs-SRCH_KO0,14.htm?clickSource=searchBox


df = df.dropna(subset=['Salary_Estimate'])


df = df.fillna('empty')  ## we do this so me can iterate through our df with lambda, otherwise we get an error


def abcd(param):
    attributes = ['Revenue', 'Industry', 'Founded', 'Type', 'Size', 'Sector']
    letters = ['a', 'b', 'c', 'd', 'e', 'f']
    
    for letter, attr in zip(letters, attributes):
        df[letter] = df[attr].apply(lambda x: x if param in x else 'empty')


# New Revenue
abcd('Revenue')

df['Revenue_v2'] = np.where(df['b'] != 'empty', df['b'], df['a'])
df['Revenue_v2'] = np.where(df['c'] != 'empty', df['c'], df['Revenue_v2'])
df['Revenue_v2'] = np.where(df['d'] != 'empty', df['d'], df['Revenue_v2'])
df['Revenue_v2'] = np.where(df['e'] != 'empty', df['e'], df['Revenue_v2'])
df['Revenue_v2'] = np.where(df['f'] != 'empty', df['f'], df['Revenue_v2'])



# New Industry
abcd('Industry')

df['Industry_v2'] = np.where(df['a'] != 'empty', df['a'], df['b'])
df['Industry_v2'] = np.where(df['c'] != 'empty', df['c'], df['Industry_v2'])
df['Industry_v2'] = np.where(df['d'] != 'empty', df['d'], df['Industry_v2'])
df['Industry_v2'] = np.where(df['e'] != 'empty', df['e'], df['Industry_v2'])
df['Industry_v2'] = np.where(df['f'] != 'empty', df['f'], df['Industry_v2'])



# New Founded
abcd('Founded')

df['Founded_v2'] = np.where(df['b'] != 'empty', df['b'], df['c'])
df['Founded_v2'] = np.where(df['a'] != 'empty', df['a'], df['Founded_v2'])
df['Founded_v2'] = np.where(df['d'] != 'empty', df['d'], df['Founded_v2'])
df['Founded_v2'] = np.where(df['e'] != 'empty', df['e'], df['Founded_v2'])
df['Founded_v2'] = np.where(df['f'] != 'empty', df['f'], df['Founded_v2'])



# New Type
abcd('Type')

df['Type_v2'] = np.where(df['b'] != 'empty', df['b'], df['d'])
df['Type_v2'] = np.where(df['c'] != 'empty', df['c'], df['Type_v2'])
df['Type_v2'] = np.where(df['a'] != 'empty', df['a'], df['Type_v2'])
df['Type_v2'] = np.where(df['e'] != 'empty', df['e'], df['Type_v2'])
df['Type_v2'] = np.where(df['f'] != 'empty', df['f'], df['Type_v2'])



# New Size
abcd('Size')

df['Size_v2'] = np.where(df['b'] != 'empty', df['b'], df['e'])
df['Size_v2'] = np.where(df['c'] != 'empty', df['c'], df['Size_v2'])
df['Size_v2'] = np.where(df['d'] != 'empty', df['d'], df['Size_v2'])
df['Size_v2'] = np.where(df['a'] != 'empty', df['a'], df['Size_v2'])
df['Size_v2'] = np.where(df['f'] != 'empty', df['f'], df['Size_v2'])


# New Sector
abcd('Sector')

df['Sector_v2'] = np.where(df['b'] != 'empty', df['b'], df['f'])
df['Sector_v2'] = np.where(df['c'] != 'empty', df['c'], df['Sector_v2'])
df['Sector_v2'] = np.where(df['d'] != 'empty', df['d'], df['Sector_v2'])
df['Sector_v2'] = np.where(df['e'] != 'empty', df['e'], df['Sector_v2'])
df['Sector_v2'] = np.where(df['a'] != 'empty', df['a'], df['Sector_v2'])


# drop columns
df = df.drop(['a', 'b', 'c', 'd', 'e', 'f', 'Revenue', 'Industry', 'Founded', 'Type', 'Size', 'Sector'], axis=1)

df.rename(columns = {'Revenue_v2': 'Revenue', 
                     'Industry_v2': 'Industry', 
                     'Founded_v2': 'Founded', 
                     'Type_v2': 'Type', 
                     'Size_v2': 'Size', 
                     'Sector_v2': 'Sector'}, inplace=True)

df.to_csv('F:/Git Documents/ds_salary_proj/glassdoor_octoparse_v2.csv')


