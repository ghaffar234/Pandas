#this programme make for read the csv file and perform  the function
import pandas as pd
#csv_1=pd.read_csv("C:\\Users\\Hp\\Downloads\\customers-100.csv",nrows=6)
#change the name of header
csv_1=pd.read_csv("C:\\Users\\Hp\\Downloads\\customers-100.csv",header=None,prefix="col")
print(csv_1)