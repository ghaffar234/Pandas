#this programme cover  all function in the pandas
import pandas as pd
import numpy as np
csv_2=pd.read_csv("C:\\Users\\Hp\\Downloads\\customers-100.csv")
#this function use for indexes measure
print(csv_2.index)
#this function use for discribe the value like min and max they work only numerical data
print(csv_2.describe)
#use this function head function to display uper latter like 5
print(csv_2.head())
#this function is use for lower value in the array or sheet
print(csv_2.tail())
#this function use to convert the value into numpy array
v=np.asarray(csv_2)
print(v)
#This is code for loc function use to tak specific value in column and row
print(csv_2.loc[[2,3],["Customer Id"]])
#this funtion is use specific one value like iloc function
print(csv_2.iloc[3,5])
#this function change the name of the column
csv_2.loc[0,"Customer Id"]="python"
print(csv_2)