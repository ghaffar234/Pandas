# this programmes make for to arrange the data in ascending order
import pandas as pd
var=pd.DataFrame({"Name":["a","b","c","d","a","d","c","b"],
                  "sr_1":[23,34,54,24,65,45,45,65],
                  "sr_2":[33,22,56,65,43,53,76,43]})
var_new=var.groupby("Name")
for x,y in var_new:
    print(x)
    print(y)
    print()
