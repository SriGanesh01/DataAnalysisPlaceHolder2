x = 5
y = 10

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import sklearn
import pandas as pd
import numpy as np
import seaborn as sns

##Naming Conventions
#UC = UnCleaned
#UM = UnMerged
#C = Cleaned
#M = Merged
#S = Sorted
#US = UnSorted
#CC = Completely Cleaned

#importing the dataset

CryptoData1_UC_M_US = pd.read_csv('DSA1\Data_Crypto_1\consolidated_coin_data.csv')
#print(CryptoData1_UC_M_US.head(10))

#Splitting the dataset with respect to currency
CryptoData1_UC_M_S = (sorted(CryptoData1_UC_M_US['Currency'].unique()))
#print(CryptoData1_UC_M_S) 
#print(CryptoData1_UC_M_US['Currency'].nunique())
#print()

for currency in CryptoData1_UC_M_US['Currency'].unique():
    CryptoData1_UC_M_US[CryptoData1_UC_M_US['Currency'] == currency].to_csv(f'DSA1\Data_Crypto_1\Split_CryptoData1\{currency}_UC.csv', index=False)

Datafile_names = [r'DSA1\Data_Crypto_1\Split_CryptoData1\binance-coin_UC.csv',
                r'DSA1\Data_Crypto_1\Split_CryptoData1\bitcoin_UC.csv',
                r'DSA1\Data_Crypto_1\Split_CryptoData1\bitcoin-cash_UC.csv',
                r'DSA1\Data_Crypto_1\Split_CryptoData1\bitcoin-sv_UC.csv',
                r'DSA1\Data_Crypto_1\Split_CryptoData1\cardano_UC.csv',
                r'DSA1\Data_Crypto_1\Split_CryptoData1\eos_UC.csv',
                r'DSA1\Data_Crypto_1\Split_CryptoData1\ethereum_UC.csv',
                r'DSA1\Data_Crypto_1\Split_CryptoData1\litecoin_UC.csv',
                r'DSA1\Data_Crypto_1\Split_CryptoData1\stellar_UC.csv',
                r'DSA1\Data_Crypto_1\Split_CryptoData1\tether_UC.csv',
                r'DSA1\Data_Crypto_1\Split_CryptoData1\tezos_UC.csv',
                r'DSA1\Data_Crypto_1\Split_CryptoData1\xrp_UC.csv']


CryptoData1_UC_UM = [] #List of unmerged Datasets
for Datafile_name in Datafile_names:
    CryptoDataFrame1 = pd.read_csv(Datafile_name)
    CryptoData1_UC_UM.append(CryptoDataFrame1)
    f = pd.read_csv(Datafile_name)
    #print(CryptoDataFrame1['Currency'].unique())
#print()

#i = 0
#for RandomName in CryptoData1_UC_UM:
    #print()
    #print(f"Head of {CryptoData1_UC_M_S[i]} {RandomName.head(10)}\n")
    #print(f"Shape of {CryptoData1_UC_M_S[i]} {RandomName.shape}\n")
    #print(f"Info of {CryptoData1_UC_M_S[i]} {RandomName.info()}\n")
    #print(f"Description of {CryptoData1_UC_M_S[i]} {RandomName.describe()}\n")
    #print(f"Sum of IsNull of {CryptoData1_UC_M_S[i]} {RandomName.isnull().sum()}\n")
    #print(f"Sum of Duplicates of {CryptoData1_UC_M_S[i]} {RandomName.duplicated().sum()}\n")
    #i+=1

##Data Cleaning

#remove null values
for CryptoDataFrame2 in CryptoData1_UC_UM:      #CryptoDataFrame(i) are separate dataframes of all split datas
    CryptoDataFrame2.dropna(inplace=True) 

#remove duplicate values
for CryptoDataFrame3 in CryptoData1_UC_UM:
    CryptoDataFrame3.drop_duplicates(inplace=True)

#convert date to datetime
for CryptoDataFrame4 in CryptoData1_UC_UM:
    CryptoDataFrame4['Date'] = pd.to_datetime(CryptoDataFrame4['Date'])
    CryptoDataFrame4['Date'] = pd.to_datetime(CryptoDataFrame4['Date'], format='%d/%m/%Y')

#print(CryptoData1_UC_UM[0].head(10))

for CryptoDataFrame5, currency in zip(CryptoData1_UC_UM, CryptoData1_UC_M_S):
    CryptoDataFrame5.to_csv(f'DSA1/Data_Crypto_1/Cleaned_CryptoData1/{currency}_C.csv', index=False)

CryptoData1_CC = []
for currency in CryptoData1_UC_M_S:
    CryptoData1_CC.append(pd.read_csv(f'DSA1/Data_Crypto_1/Cleaned_CryptoData1/{currency}_C.csv'))

#print(CryptoData1_CC[0].head(10))

#Basic Stats
for df, currency in zip(CryptoData1_CC, CryptoData1_UC_M_S):
    print(f"\nSummary statistics for {currency}:")
    print(df.describe())

# Correlation Analysis
Matrix_Names = []
for df, currency in zip(CryptoData1_CC, CryptoData1_UC_M_S):
    print(f"\nCorrelation matrix for {currency}:")
    numeric_columns = df.select_dtypes(include=[np.number]).columns
    correlation_matrix = df[numeric_columns].corr()

    if not correlation_matrix.empty:
        print(correlation_matrix)

        sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')
        plt.title(f'Correlation Matrix - {currency}')
        save_path = f'DSA1/static/images/CorrImg/{currency}_Correlation_Matrix.png'
        plt.savefig(save_path)
        Matrix_Names.append(f'{currency}_Correlation_Matrix.png')

lengthOf = (len(Matrix_Names))
print(Matrix_Names)

