#this is first programme of pandas and use data structures
import pandas as pd
var1=pd.Series([1,3,4,6,8,6,4])
print(var1)
#this programme make for use dictionary in the pandas
dic={"name":["ghaffar","Ahmad ameen","Ahmad butt"],
     "rank":[1,2,3],
     "career":["data engineer","web developer","bussiness man"]}
var2=pd.Series(dic)
print(var2)
#this programme make for data missing operation
var3=pd.Series(12,index=[1,2,3,4,5,6])
var4=pd.Series(12,index=[1,2,3])
sum=var3+var4
print(sum)