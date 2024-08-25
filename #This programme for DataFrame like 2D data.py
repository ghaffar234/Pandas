#This programme for DataFrame like 2D data set
import pandas as pd
var1=[[1,2,3,4,5,6],[4,5,6,7,8,8]]
var2=pd.DataFrame(var1,index=["a","b"])
print(var2)
#for get any number in the data use column and row
print(var2[3]["b"])
#use any dictionary in the data set
dic={"a":[1,2,2,2,3,4,4],1:[2,5,6,6,7,5,4],"c":[1,1,8,6,4,2,1]}
dic2=pd.DataFrame(dic,index=[1,2,3,4,5,6,7])
print(dic2)