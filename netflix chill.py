import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df=pd.read_csv("8. Netflix Dataset.csv")
df.head()

#checking the no. of rows and coloumns
df.shape

#list down all the columns name
df.columns

#checking datatype
df.info()

#checking duplicate value
df[df.duplicated()]

#drop the duplicates
df.drop_duplicates(inplace= True)
df[df.duplicated()]

#check the knull value
df.isnull().sum()

#using heat-map to show null value count
plt.figure(figsize = [10,6])
sns.heatmap(df.isnull())

#to show all the records of a particular item in any coloumn
df[df['Title'].isin(['Zindegi na milegi Dobara'])]

#formatting release_date column
df['Date']= pd.to_datetime(df['Release_Date'])
df.head()

df['Date'].dt.year.value_counts()

#show with the bar graph
df['Date'].dt.year.value_counts().plot(kind = 'bar')

df['Category'].value_counts()

plt.figure(figsize = [10,6])
#df['Category'].value_counts().plot(kind = 'bar')
sns.countplot(df['Category'])

df['Year'] = df['Date'].dt.year
df.head()

df[(df['Category'] == 'Movie') & (df['Year'] == 2016)].head()

df[(df['Category'] == 'Tv Show') & (df['Country'] == 'India')]['Title']

df['Director'].value_counts().head()

df[(df['Category'] == 'Movie') & (df['Type'] == 'Comedies') | (df['Country'] == 'India')].head()

#drop the null values
new_df = df.dropna()
new_df.head()

new_df[new_df['Cast'].str.contains('Rajneesh Duggal')]

new_df['Rating'].unique()

new_df[(new_df['Rating'] == 'TV-14') & (new_df['Country'] == 'India')].head()

country_with_highest_no_of_tvshows = new_df[new_df['Category'] == 'TV Show']
country_with_highest_no_of_tvshows.head()

country_with_highest_no_of_tvshows.Country.value_counts().head()

plt.figure(figsize = [8,4])
country_with_highest_no_of_tvshows.Country.value_counts().plot(kind = 'bar')




