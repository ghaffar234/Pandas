#this programme make for insert and delete the column in the pandas
import pandas as pd
var1=pd.DataFrame({"A":[1,3,4,6],"B":[3,5,6,4],"C":[6,4,8,5]})
var1.insert(3,"D",[4,9,8,7])
var1.insert(4,"E",var1["B"])
#delete the any column of any pandas
var1.pop("D")
print(var1)