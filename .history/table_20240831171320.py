import pandas as pd
from tabulate import tabulate

# Create the DataFrame
var1 = pd.DataFrame({
    "Student_Name": ["ghaffar", "ahmad", "butt", "abdullah", "ahsan", "ali"],
    "English": [23, 43, 12, 42, 32, 21],
    "Math": [26, 21, 56, 43, 21, 25]
})

# Create the pivot table
var2 = var1.pivot_table(index="Student_Name", values=["Math", "English"], aggfunc="sum", margins=False)

# Format using tabulate
colored_output = tabulate(
    var2,
    headers='keys',
    tablefmt="fancy_grid",
    showindex=True
)

print(colored_output)