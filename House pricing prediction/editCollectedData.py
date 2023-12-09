import pandas as pd

df = pd.read_csv(r"..\CSVs\UneditedDataSet.csv", encoding="utf-16", index_col=0)

df = df.drop("Vizionare la distanță", axis= 1)
df = df.replace('Cere informații', pd.NA)
df = df.replace('fără informații', pd.NA)
df["Numărul de camere"] = df["Numărul de camere"].replace("mai mult de 10", '>10')

df.to_csv(r"..\CSVs\EditedDataSet.csv", encoding="utf-16")
df.to_csv(r"..\CSVs\EditedDataSet--tab-separated.csv", encoding="utf-16", sep="\t")