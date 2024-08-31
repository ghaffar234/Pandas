#this code is make for to use the pivot aur create table in the python
import pandas as pd
var1=pd.DataFrame({"Days":[1,2,3,4,5,6],
                   "Student_Name":["ghaffar","ahmad","butt","abdullah","ahsan","ali"],
                   "English":[23,43,12,42,32,21],"Math":[26,21,56,43,21,25]})
var2=var1.pivot(index="Days",columns="Student_Name",aggfunc="English")
var2.fillna(int(0),inplace=True)
print(var2)