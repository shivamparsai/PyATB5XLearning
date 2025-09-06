import csv
import pandas as pd

# with open(r"C:\Users\DELL\PycharmProjects\PyATB5XLearning\DEC\ex_07122024_Exceptions\TestData.csv") as csvFile:
#     r = csv.reader(csvFile)
#     for col in r:
#         print(col[0], col[1], sep="|")

o = pd.read_csv(r"C:\Users\DELL\PycharmProjects\PyATB5XLearning\DEC\ex_07122024_Exceptions\TestData.csv")
print(o)