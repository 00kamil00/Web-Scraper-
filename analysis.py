import pandas as pd 
import matplotlib.pyplot as plt 

df = pd.read_csv('countries.csv')

population = df['population']
area = df['area']

df['density'] = population / area 
#print(df.columns)


#df.to_csv('countries_density.csv', index=False)

top_10 = df.sort_values(by='population', ascending=False).head(10)


#creating a graph 
plt.bar(top_10['country'], top_10['population']) #x = country, y = population

plt.xlabel("country")
plt.ylabel("population")
plt.title("countries population graph")

for i, val in enumerate(top_10['population']):
    plt.text(i, val, str(val), ha='center', va='bottom')

plt.show()
