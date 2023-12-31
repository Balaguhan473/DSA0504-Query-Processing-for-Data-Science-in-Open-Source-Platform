import pandas as pd
employees = pd.read_csv(r"EMPLOYEES.csv")
departments = pd.read_csv(r"DEPARTMENTS.csv")
job_history = pd.read_csv(r"JOB_HISTORY.csv")
jobs = pd.read_csv(r"JOBS.csv")
countries = pd.read_csv(r"COUNTRIES.csv")
regions = pd.read_csv(r"REGIONS.csv")
locations = pd.read_csv(r"LOCATIONS.csv")
print("job_id Job ID min_salary max_salary")
result = jobs.sort_values('job_title')
for index, row in result.iterrows():
print(row['job_id'].ljust(15),row['job_title'].ljust(35),str(row['min_salary']).ljust(9),row['max_salary'])
