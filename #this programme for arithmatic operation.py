#this programme for arithmatic operation the pandas
import pandas as pd
var={"A":[1,34,5,6],"B":[5,6,33,66]}
var2=pd.DataFrame(var)
var2["Sum"]=var2["A"] + var2["B"]
#this for product
var2["Product"]=var2["A"] * var2["B"]
#this code for division
var2["Division"]=var2["A"] / var2["B"]
#this code for subtraction 
var2["Subtraction"]=var2["A"] - var2["B"]
#this code for modulus
var2["modulus"]=var2["A"] % var2["B"]
var2["condition in Sum"]=var2["Sum"] >=40
print(var2)