import pandas as pd
import numpy as np

#1) Create Series
s = pd.Series([10,20,30])
print(s)

#2) Create DataFrame
df = pd.DataFrame({
    'Name': ['Navid','Hari','Kumar','Maya','Praveen'],
    'Age': [25,30, np.nan, 30,25],
    'Salary': [20000, 40000, 50000, 25000, 35000]
})

print("DATAFRAME")
print(df)

#3)View Data
print("Head:",df.head())
print("Tail:",df.tail())
print("Shape:",df.shape)
print("columns:",df.columns)
print("index:",df.index)
print("dtypes:",df.dtypes)

#4)Select Columns
print("Single column:\n",df['Name']) #printing a column named Name
print("Multiple column:\n",df[['Name','Salary']])

#5)Select rows
print("Single row:\n",df.iloc[0]) #printing first row
print("Multiple rows:\n",df.iloc[0:2])

#6)Filter Data
print("Single condition:\n",df[df['Salary'] > 30000])
print("Multiple condition:\n",df[(df['Salary'] > 30000) & (df['Age'] > 20)])

#7)Adding and deleting columns
df['Bonus'] = 5000
print("After adding bonus:\n",df)
df = df.drop(columns=['Bonus'])
print("After deleting bonus:\n",df)

#8)Update values
df.loc[df['Name'] == 'Navid','Salary'] = 45000
print(df)

#9)Delete Row 
df_deleted_rows = df.drop(index=0) 
print(df_deleted_rows)

#10)Sort
print("Ascending:\n",df.sort_values(by = 'Salary', ascending=True))
print("Descending:\n",df.sort_values(by='Salary',ascending=False))

#11)Remove missing values
df_without_missing_val = df
print(df_without_missing_val.dropna())

#12)Filling missing values
df['Age'] = df['Age'].fillna(df['Age'].mean())
print(df)

#13)stats
print("Sum:",df['Salary'].sum())
print("Mean:",df['Salary'].mean())
print("Median:",df['Salary'].median)
print("Max:",df['Salary'].max())
print("Min:",df['Salary'].min())
print("Std:",df['Salary'].std())

#14)Group by
print(df.groupby('Name')['Salary'].mean())

#15)Read/save CSV & Remove duplicates
df.to_csv('data.csv',index=False)
df_read = pd.read_csv('data.csv')
print("Read from csv\n:",df_read)
print("Remove Duplicates\n:",df.drop_duplicates())

#16)Rename column
df_renamed = df.rename(columns={'Salary':'Payment'})
print(df_renamed)


