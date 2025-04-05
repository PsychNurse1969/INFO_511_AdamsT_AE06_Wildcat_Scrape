# AE 01: Meet the Penguins #

# This will import pandas and seaborn packages

import pandas as pd
import seaborn as sns

# This will load the dataset "penguins" 

penguins = sns.load_dataset("penguins")

# add code here# add code here
penguins.info()

# This will calculate the number of rows in the penguin data frame #

num_rows = len(penguins)

# This will display the number of rows in the dataset #

print("Number of rows:", num_rows)  # Print number of rows

print(f"There are {num_rows} in the penguins data frame")

# I'm unclear on why this code was included in the ae-meet-the-penguins exercise #

x = 2
result = x * 3
print(result)

# I used ChatGPT to help mre resolve the dataset link