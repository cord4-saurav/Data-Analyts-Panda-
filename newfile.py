import pandas as pd

panda = pd.read_csv(r"~/Downloads/cheat sheets/archive/covid_19_india.csv")
# print('hfgfgf')
# print(panda)
print(panda.head())#  #it show the total n rows in dataframe
# print(panda.shape)  # it shows rows and column
# print(panda.index)  # provides attribute of dataframes
# print(panda.columns) # shows total columns of dataframe
print(panda.dtypes) # datatypes of each column
# print(panda['State/UnionTerritory'].unique()) #it will show the unique value of a particular column
# print(panda.nunique()) # it will show the unique value of particular column or for a whole dataframe
# print(panda.count()) # it will show the no null-value in each column
# print(panda['State/UnionTerritory'].value_counts()) # it will show the unique value in single column
# print(panda.info()) # provides basic information about the dataframe


# finding the unique value in dataframe ?

# print(panda['ConfirmedForeignNational'].unique())
# print(panda.head(2))
# print(panda['ConfirmedForeignNational'].nunique())

# print(panda.head())
# print(panda.index)  # provides attribute of dataframes
# print(panda.)
# print(panda['Confirmed'].value_counts())
# print(panda.Confirmed.value_counts())

### How to Filer the data from Dataframe

# print(panda[panda['State/UnionTerritory'] == 'State/UnionTerritory'])


### Groupby() is used to get specific data from column

# print(panda.groupby("Deaths").get_group('Deaths'))

## To Find NotNull From Dataframe
# print(panda.isnull().sum())
# print(panda.notnull().sum())



##### How To Rename The Column
# print(panda.head(2))
#
# print(panda.rename(columns={'Cured': 'Peoples Cured'}), inplace=True)



## How to find the mean value

# print(panda['Sno'].mean())

## standard deviation

# print(panda['Sno'].std())

## What is the variance

# print(panda['Sno'].var())


## Find All the Instances

# print(panda['State/UnionTerritory'].value_counts())

# print[panda(panda['State/UnionTerritory'] == 'Himanchal Pradesh')]

## To find the two data parallely

# print[panda['State/UnionTerritory'] & panda['Sno']]


## How to find the mean value of each column

# print(panda.groupby('Time').mean())


## How to find the max and min for each column

# print(panda.groupby('Time').max())
# print(panda.groupby('Time').min())



