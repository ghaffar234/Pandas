#this programme for the remove the null value and put new value
import pandas as pd
var=pd.read_csv("C:\\Users\\Hp\\Downloads\\paractice sheet 1 null value.csv")
#this function use as the fill value in null value
print(var.fillna("Ghaffar"))
#this function is used for drop the null value row
#print(var.dropna())
#This function is use for fill the forward and backword filing
#print(var.dropna(how="any"))
#fill any value in the null position of sheet
print(var.fillna(13,inplace=True))
