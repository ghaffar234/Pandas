#This programme make for to concat the  two data frames
import pandas as pd
d1=pd.DataFrame({"A":[2,3,4,5],"B":[6,4,7,4]})
d2=pd.DataFrame({"A":[2,3,4,5],"C":[4,5,6,3]})
var3=pd.concat([d1,d2],axis=1)
print(var3)