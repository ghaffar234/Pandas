# make the programme for make the csv file
import pandas as pd
dic={"A":[2,5,4,2],"C":[5,3,2,5],"G":[64,47,44,8]}
d=pd.DataFrame(dic)
d.to_csv("Ghaffar.csv")
print(d)