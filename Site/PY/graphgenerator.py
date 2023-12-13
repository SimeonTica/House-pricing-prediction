
import pandas as pd

import numpy as np

import matplotlib.pyplot as plt
import seaborn as sns

def replaceCategoriesWithNumbers():
    categoryDict = {}

    for column in df:
        if(not df[column].astype(str).str.contains(r'\d', na=False).any()):
            columnCategories = pd.Categorical(df[column])

            columnDict = {}
        
            for index, category in enumerate(columnCategories.categories):
                columnDict[category] = index + 1

            categoryDict[column] = columnDict

    for column in categoryDict:
        for label in categoryDict[column]:
            df[column] = df[column].replace(label, categoryDict[column][label])


    return categoryDict


def replaceNumbersWithCategories(df):
    for column in categoryDict:
        for label in categoryDict[column]:
            df[column] = df[column].replace(categoryDict[column][label], label)
        df[column] = df[column].replace(0, "Neprecizat")


def removeOutliers(column, df):

    percentile25 = df   [column].quantile(0.25)
    percentile75 = df[column].quantile(0.75)
    iqr = percentile75-percentile25
    upper_limit = percentile75 + 1.5 * iqr
    lower_limit = percentile25 - 1.5 * iqr
    new_df = df[df[column] < upper_limit]
    # new_df = new_df[df[column] > lower_limit]

    return new_df

def capOutliers(column, df):
    percentile25 = df   [column].quantile(0.25)
    percentile75 = df[column].quantile(0.75)
    iqr = percentile75-percentile25
    upper_limit = percentile75 + 1.5 * iqr
    lower_limit = percentile25 - 1.5 * iqr
    new_df_cap = df.copy()
    new_df_cap[column] = np.where(
    new_df_cap[column] > upper_limit,
    upper_limit,
    np.where(
        new_df_cap[column] < lower_limit,
        lower_limit,
        new_df_cap[column]))
    return new_df_cap

df = pd.read_csv(r"CSVs\EditedDataSet.csv", encoding="utf-16", index_col=0)

dfWithLabels = df.copy()

categoryDict = replaceCategoriesWithNumbers()

replaceNumbersWithCategories(dfWithLabels)
        

fig_size = plt.rcParams["figure.figsize"]

fig_size[0] = 10

fig_size[1] = 8

plt.rcParams["figure.figsize"] = fig_size

sns.set_theme()
df.info()
dfWithLabels.Stare.value_counts()
dfWithLabels["Garaj/loc de parcare"].value_counts()
dfWithLabels["Suprafață teren (m²)"].value_counts()

sns.histplot(df['Pret'], kde=False, bins=500)
plt.xlim(0, 1e7 * 0.5)
plt.savefig('Site\Photos\output1.png') 
plt.close() 
#plt.show()
sns.lineplot(x="Suprafață", y="Pret", data=df)
plt.savefig('Site\Photos\output2.png') 
plt.close() 
sns.barplot(x="Pret", y="Tip încălzire", data=dfWithLabels)
plt.savefig('Site\Photos\output3.png') 
plt.close() 
sns.scatterplot(x="Suprafață teren (m²)", y="Pret", data=df)
plt.xlim(0, 3500)
plt.savefig('Site\Photos\output4.png') 
plt.close() 
sns.barplot(x="Pret", y="Stare", data=dfWithLabels)
plt.savefig('Site\Photos\output5.png') 
plt.close() 
sns.barplot(x="Tip clădire", y="Pret", data=dfWithLabels)
plt.savefig('Site\Photos\output6.png') 
plt.close() 
sns.lineplot(x="Anul construcției", y="Pret", data=df)
plt.xlim(1850, 2050)
plt.savefig('Site\Photos\output7.png') 
plt.close() 
sns.barplot(x="Numărul de camere", y="Pret", data=df)
plt.savefig('Site\Photos\output8.png') 
plt.close() 
sns.barplot(x="Garaj/loc de parcare", y="Pret", data=dfWithLabels)
plt.savefig('Site\Photos\output9.png') 
plt.close() 
sns.barplot(x="Tip proprietate", y="Pret", data=dfWithLabels)
plt.savefig('Site\Photos\output10.png') 
plt.close() 
sns.barplot(x="Pret", y="Material de construcție", data=dfWithLabels)
plt.savefig('Site\Photos\output11.png') 
plt.close() 
sns.lineplot(x="Numar de etaje", y="Pret", data=dfWithLabels)
plt.savefig('Site\Photos\output12.png') 
plt.close() 
sns.barplot(x="Tip acoperis", y="Pret", data=dfWithLabels)
plt.savefig('Site\Photos\output13.png') 
plt.close() 
sns.barplot(x="Acoperis", y="Pret", data=dfWithLabels)
plt.savefig('Site\Photos\output14.png') 
plt.close() 
sns.barplot(x="Tip mansardă", y="Pret", data=dfWithLabels)
plt.savefig('Site\Photos\output15.png') 
plt.close() 
sns.barplot(x="Pret", y="Tip acces", data=dfWithLabels)
plt.savefig('Site\Photos\output16.png') 
plt.close() 
sns.barplot(x="Locație", y="Pret", data=dfWithLabels)
plt.savefig('Site\Photos\output17.png') 
plt.close() 
sns.barplot(x="Aer condiționat", y="Pret", data=dfWithLabels)
plt.savefig('Site\Photos\output18.png') 
plt.close() 
df.hist(bins=50, figsize=(20,15))
plt.savefig('Site\Photos\output19.png') 
plt.close() 
new_df = removeOutliers("Suprafață", df)
new_df = removeOutliers("Suprafață teren (m²)", new_df)
new_df = removeOutliers("Pret", new_df)
new_df_cap = capOutliers("Suprafață", df)
new_df_cap = capOutliers("Suprafață teren (m²)", new_df_cap)
new_df_cap = capOutliers("Pret", new_df_cap)

new_df.hist(figsize=(20, 14))
plt.savefig('Site\Photos\output20.png') 
plt.close() 

new_df_cap.Pret.value_counts()
new_df_cap.hist(figsize=(20,14))
plt.savefig('Site\Photos\output21.png') 
plt.close() 

