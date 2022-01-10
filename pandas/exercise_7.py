import pandas as pd


file = pd.read_csv("iris.csv")
data = file.groupby("variety")
d1 = file[file["variety"] == "Setosa"]
d2 = file[file["variety"] == "Versicolor"]
d3 = file[file["variety"] == "Virginica"]

with pd.ExcelWriter('iris2.xlsx') as writer:
    d1.to_excel(writer, sheet_name='Setosa')
    d2.to_excel(writer, sheet_name='Versicolor')
    d3.to_excel(writer, sheet_name='Virginica')
