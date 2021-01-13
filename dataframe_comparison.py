#import necessary packages
import pandas as pd
import numpy as np

#extract the files to dataframe for comparison
df1 = pd.read_csv('data_file1.csv')
df2 = pd.read_csv('data_file2.csv')

comparison_values = df1.values == df2.values
print (comparison_values) #prints the cell values True/False

df1.equals(df2)
#return True if dataframes match else returns False

#export each cell value into a numpy array
rows,cols=np.where(comparison_values==False)

#for each cell which are False, write the cell values sepearted by --> which will be easy for checking
for item in zip(rows,cols):
    df1.iloc[item[0], item[1]] = '{} --> {}'.format(df1.iloc[item[0], item[1]],df2.iloc[item[0], item[1]])

#export the comparison results to an excel file
df1.to_excel('Excel_datasource_comparison.xlsx',index=False,header=True)
