#this function is used to join the data frames and data sets
import pandas as pd
var1=pd.DataFrame({"A":[3,24,6,23],"B":[23,53,14,64]})
var2=pd.DataFrame({ "C":[3,42,53,53],"D":[32,76,43,77]})
#var3=var1.join(var2)
#var3["Sum"]=var1["A"] +var2["C"]
#print(var3)
#use this code to use append function
var5=var1.append(var2,ignore_index=True)
#this code for make put the value in the null place 
var5.fillna("ghaffar",inplace=True)
print(var5)