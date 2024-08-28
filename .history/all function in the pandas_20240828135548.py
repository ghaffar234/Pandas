#this programme cover  all function in the pandas
import pandas as pd
csv_2=pd.read_csv("C:\\Users\\Hp\\Downloads\\customers-100.csv")
#this function use for indexes measure
print(csv_2.index)
#this function use for discribe the value like min and max they work only numerical data
print(csv_2.describe)
#use this function head function to display uper latter like 5
print(csv_2.head())