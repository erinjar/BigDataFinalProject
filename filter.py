import pandas as pd

print("This tool will filter one dataset by another, using the common columns.")

csv1 = str(input("Enter the name of the first csv file. This will be the filter: ")) + ".csv"
csv2 = str(input("Enter the name of the second csv file. This will be filtered: ")) + ".csv"


df1 = pd.read_csv(csv1)
df2 = pd.read_csv(csv2)

c_csv1 = str(input("What is the column name of the first csv file? "))
c_csv2 = str(input("What is the column name of the second csv file? "))

filtered_df2 = df2[df2[c_csv2].isin(df1[c_csv1])]

output = str(input("What do you want to call the output file? ")) + ".csv"

filtered_df2.to_csv(output, index=False)

print("Filtered data saved to " + str(output))