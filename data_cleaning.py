# author: bashar 

import pandas as pd

df = pd.read_csv('glassdoor_jobs.csv')
# show = df.head()
# print(show)

#salary parsing 

df['hourly'] = df['Salary Estimate'].apply(lambda x: 1 if 'per hour' in x.lower() else 0)
df['employer_provided'] = df['Salary Estimate'].apply(lambda x: 1 if 'employer provided salary:' in x.lower() else 0)

df = df[df['Salary Estimate'] != '-1'] # remove rows without salary estimate

salary =df ['Salary Estimate'].apply(lambda x: x.split('(')[0]) 

minus_Kd = salary.apply(lambda x: x.replace('K','').replace('$',''))  

min_hr = minus_Kd.apply(lambda x: x.lower().replace('per hour', '').replace('employer provided salary:', ''))

df['min_salary'] = min_hr.apply(lambda x: int(x.split('-')[0]))
df['max_salary'] = min_hr.apply(lambda x: int(x.split('-')[1]))
df['avg_salary'] = (df.min_salary + df.max_salary) / 2
# show = df[['min_salary', 'max_salary', 'avg_salary']].head(10)
# print(show)

# Company name text only 

df['company_txt'] = df.apply(lambda x: x['Company Name'] if x['Rating'] < 0 else x['Company Name'][:-3], axis=1) 
# show = df['company_txt'].head(10)
# print(show)

#state field 
df['job_state'] = df['Location'].apply(lambda x: x.split(',')[1])
df.job_state.value_counts()


df['same_state'] = df.apply(lambda x: 1 if x.Location == x.Headquarters else 0, axis=1) #If job is in same state as headquarters

#age of company 
df['age'] = df.Founded.apply(lambda x: x if x < 1 else 2025 - x)
# show = df[['Company Name', 'Founded', 'age']].head(10)
# print(show)

#parsing of job description (python, etc.)

#python
df['python_yn'] = df['Job Description'].apply(lambda x: 1 if 'python' in x.lower() else 0)

#R studio
df['R_yn'] = df['Job Description'].apply(lambda x: 1 if 'r studio' in x.lower() or 'r-studio' in x.lower() else 0)
#spark
df['spark'] = df['Job Description'].apply(lambda x: 1 if 'spark' in x.lower() else 0)
#aws
df['aws'] = df['Job Description'].apply(lambda x: 1 if 'aws' in x.lower() else 0)
#excel
df['excel'] = df['Job Description'].apply(lambda x: 1 if 'excel' in x.lower() else 0)
#sql
df['sql'] = df['Job Description'].apply(lambda x: 1 if 'sql' in x.lower() else 0)
#tableau
df['tableau'] = df['Job Description'].apply(lambda x: 1 if 'tableau' in x.lower() else 0)
#power bi
df['power_bi'] = df['Job Description'].apply(lambda x: 1 if 'power bi' in x.lower() else 0)
#pytorch
df['pytorch'] = df['Job Description'].apply(lambda x: 1 if 'pytorch' in x.lower() else 0)
#tensorflow
df['tensorflow'] = df['Job Description'].apply(lambda x: 1 if 'tensorflow' in x.lower() else 0)
#scikitlearn
df['scikitlearn'] = df['Job Description'].apply(lambda x: 1 if 'scikit-learn' in x.lower() or 'sklearn' in x.lower() else 0)


#show final data
df_out = df.drop(['Unnamed: 0'], axis=1)

df_out.to_csv('salary_data_cleaned.csv', index=False)