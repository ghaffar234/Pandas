#This programme make for to merge the data 
from operator import index
import pandas as pd
var1=pd.DataFrame({"A":[2,3,4,5],"B":[4,5,6,7]})
var2=pd.DataFrame({"A":[2,3,4,5],"C":[4,2,5,7]})
var3=pd.merge(var1,var2,on="A")
var4 = pd.Series(var3["B"].values, index=["a", "b", "c", "d"])
print(var4)