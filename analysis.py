import pandas as pd 

df = pd.read_csv('countries.csv')

population = df['population']
area = df['area']

df['density'] = population / area 
print(df.columns)


df.to_csv('countries_density.csv', index=False)
