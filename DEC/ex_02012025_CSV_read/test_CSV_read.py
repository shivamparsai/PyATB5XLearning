import csv
import pandas as pd
import pytest
import allure

class Test_Read():
    def test_read_csv(self):
        with open("UserData.csv") as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                print(row[0], row[1])

    def test_read_pandas(self):
        df = pd.read_csv("UserData.csv")
        print(df)
