import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def createPlots():

    df = pd.read_csv(r"..\..\..\CSVs\EditedDataSet--with-categories.csv", encoding="utf-16", index_col=0)

    sns.histplot(df['Pret'], kde=False, bins=500)
    plt.xlim(0, 1e7 * 0.5)
    plt.tight_layout()
    plt.savefig('..\..\Photos\output1.png') 
    plt.close() 
    #plt.show()
    sns.lineplot(x="Suprafață", y="Pret", data=df)
    plt.tight_layout()
    plt.savefig('..\..\Photos\output2.png') 
    plt.close() 
    sns.barplot(x="Pret", y="Tip încălzire", data=df)
    plt.tight_layout()
    plt.savefig('..\..\Photos\output3.png') 
    plt.close() 
    sns.scatterplot(x="Suprafață teren (m²)", y="Pret", data=df)
    plt.tight_layout()
    plt.xlim(0, 3500)
    plt.savefig('..\..\Photos\output4.png') 
    plt.close() 
    sns.barplot(x="Pret", y="Stare", data=df)
    plt.tight_layout()
    plt.savefig('..\..\Photos\output5.png') 
    plt.close() 
    sns.barplot(x="Tip clădire", y="Pret", data=df)
    plt.tight_layout()
    plt.savefig('..\..\Photos\output6.png') 
    plt.close() 
    sns.lineplot(x="Anul construcției", y="Pret", data=df)
    plt.xlim(1850, 2050)
    plt.tight_layout()
    plt.savefig('..\..\Photos\output7.png') 
    plt.close() 
    sns.barplot(x="Numărul de camere", y="Pret", data=df)
    plt.tight_layout()
    plt.savefig('..\..\Photos\output8.png') 
    plt.close() 
    sns.barplot(x="Garaj/loc de parcare", y="Pret", data=df)
    plt.tight_layout()
    plt.savefig('..\..\Photos\output9.png') 
    plt.close() 
    sns.barplot(x="Tip proprietate", y="Pret", data=df)
    plt.tight_layout()
    plt.savefig('..\..\Photos\output10.png') 
    plt.close() 
    sns.barplot(x="Pret", y="Material de construcție", data=df)
    plt.tight_layout()
    plt.savefig('..\..\Photos\output11.png') 
    plt.close() 
    sns.lineplot(x="Numar de etaje", y="Pret", data=df)
    plt.tight_layout()
    plt.savefig('..\..\Photos\output12.png') 
    plt.close() 
    sns.barplot(x="Tip acoperis", y="Pret", data=df)
    plt.tight_layout()
    plt.savefig('..\..\Photos\output13.png') 
    plt.close() 
    sns.barplot(x="Acoperis", y="Pret", data=df)
    plt.tight_layout()
    plt.savefig('..\..\Photos\output14.png') 
    plt.close() 
    sns.barplot(x="Tip mansardă", y="Pret", data=df)
    plt.tight_layout()
    plt.savefig('..\..\Photos\output15.png') 
    plt.close() 
    sns.barplot(x="Pret", y="Tip acces", data=df)
    plt.tight_layout()
    plt.savefig('..\..\Photos\output16.png') 
    plt.close() 
    sns.barplot(x="Locație", y="Pret", data=df)
    plt.tight_layout()
    plt.savefig('..\..\Photos\output17.png') 
    plt.close() 
    sns.barplot(x="Aer condiționat", y="Pret", data=df)
    plt.tight_layout()
    plt.savefig('..\..\Photos\output18.png') 
    plt.close() 
    df.hist(bins=50, figsize=(20,15))
    plt.tight_layout()
    plt.savefig('..\..\Photos\output19.png') 
    plt.close() 

    new_df = pd.read_csv(r"..\..\..\CSVs\EditedDataSet_df-out-removed.csv", encoding="utf-16", index_col=0)
    new_df_cap = pd.read_csv(r"..\..\..\CSVs\EditedDataSet_df-cap.csv", encoding="utf-16", index_col=0)

    new_df.hist(figsize=(20, 14))
    plt.savefig('..\..\Photos\output20.png') 
    plt.close() 

    new_df_cap.Pret.value_counts()
    new_df_cap.hist(figsize=(20,14))
    plt.savefig('..\..\Photos\output21.png')
    plt.close()