# Data-Cleaning-In-Pandas
import pandas as pd
df = pd.read_excel(r"C:\Users\ADERONKE\Downloads\Customer Call List.xlsx")
df
df.drop_duplicates()
df = df.drop(columns = "Not_Useful_Column")
df
