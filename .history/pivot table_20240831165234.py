#this code is make for to use the pivot aur create table in the python
import pandas as pd
from tabulate import tabulate
from colorama import Fore, Style,init
init()
var1=pd.DataFrame({"Days":[1,2,3,4,5,6],
                   "Student_Name":["ghaffar","ahmad","butt","abdullah","ahsan","ali"],
                   "English":[23,43,12,42,32,21],"Math":[26,21,56,43,21,25]})
#This use to for particule one value
#var2=var1.pivot_table(index="Days",columns="Student_Name",values="English")
#var2.fillna(int(0),inplace=True)
#print(var2)
#use of the pivot table to perform various function in the function
var2=var1.pivot_table(index="Days",columns="Student_Name",aggfunc="sum",margins=True)
var2.fillna(0,inplace=True)
colored_output = tabulate(var2,headers=[Fore.RED + "Days" + Style.RESET_ALL] + [Fore.GREEN + col + Style.RESET_ALL for col in var2.columns.levels[1]],
    tablefmt="fancy_grid",
    stralign="center",
    numalign="center"
)

print(colored_output)