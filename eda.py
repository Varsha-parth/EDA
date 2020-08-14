# -*- coding: utf-8 -*-
"""EDA(coursera).ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1GT9lsIMb7FXR-fJtIkRcHCuFFwZ2EQ_m
"""

from google.colab import files
insurance = files.upload()

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import statsmodels.api as sm
import scipy.stats as st
from sklearn.preprocessing import LabelEncoder
sns.set()

insurance_df = pd.read_csv("datasets_15325_20391_insurance.csv")
insurance_df.head()

insurance_df.info()

insurance_df.isna().apply(pd.value_counts)

plt.figure(figsize=(20,15))
plt.subplot(3,1,1)
sns.boxplot(x=insurance_df.bmi,color="red")

plt.subplot(3,1,2)
sns.boxplot(x=insurance_df.age,color="blue")

plt.subplot(3,1,3)
sns.boxplot(x=insurance_df.charges,color="green")

plt.show()

insurance_df.describe()

plt.figure(figsize=(20,15))
plt.subplot(3,3,1)
plt.hist(x=insurance_df.bmi, color="pink", alpha=0.7, edgecolor="black") 
plt.xlabel("bmi")

plt.subplot(3,3,2)
plt.hist(x=insurance_df.age, color="orange", alpha=0.7, edgecolor="black") 
plt.xlabel("age")

plt.subplot(3,3,3)
plt.hist(x=insurance_df.charges, color="yellow", alpha=0.7, edgecolor="black") 
plt.xlabel("charges")
plt.show()

skewness=pd.DataFrame({'Skewness':[st.skew(insurance_df.bmi),st.skew(insurance_df.age),st.skew(insurance_df.charges)]},index=['bmi','age','charges'])
skewness

plt.figure(figsize=(20,25))
x=insurance_df.smoker.value_counts().index
y=[insurance_df["smoker"].value_counts()[i] for i in x]

plt.subplot(4,2,1)
plt.bar(x,y,color="lightblue",alpha=0.7,edgecolor="black")
plt.xlabel("smoker")
plt.ylabel("count")
plt.title("Smoker Distribution")

x1=insurance_df.sex.value_counts().index
y1=[insurance_df["sex"].value_counts()[i] for i in x1]

plt.subplot(4,2,2)
plt.bar(x1,y1,color="lightblue",alpha=0.7,edgecolor="black")
plt.xlabel("sex")
plt.ylabel("count")
plt.title("Sex Distribution")

x2=insurance_df.region.value_counts().index
y2=[insurance_df["region"].value_counts()[i] for i in x2]

plt.subplot(4,2,3)
plt.bar(x2,y2,color="lightblue",alpha=0.7,edgecolor="black")
plt.xlabel("region")
plt.ylabel("count")
plt.title("region Distribution")

x3=insurance_df.children.value_counts().index
y3=[insurance_df["children"].value_counts()[i] for i in x3]

plt.subplot(4,2,4)
plt.bar(x3,y3,color="lightblue",alpha=0.7,edgecolor="black")
plt.xlabel("children")
plt.ylabel("count")
plt.title("Children Distribution")

plt.show()

import copy
insurance_df_encoded=copy.deepcopy(insurance_df)
insurance_df_encoded.loc[:,['sex','smoker','region']]=insurance_df_encoded.loc[:,['sex','smoker','region']].apply(LabelEncoder().fit_transform)
sns.pairplot(insurance_df_encoded)
plt.show()

insurance_df.smoker.value_counts()

plt.figure(figsize=(20,15))
plt.subplot(2,2,1)
sns.scatterplot(insurance_df.age,insurance_df.charges,hue=insurance_df.smoker,palette=['red','green'])

plt.subplot(2,2,2)
sns.scatterplot(insurance_df.age,insurance_df.charges,hue=insurance_df.sex,palette=['pink','lightblue'])
plt.show()

h0="Charges of smokers and non smokers are the same "
ha="Charges of smokers and non smokers are not the same"
x=np.array(insurance_df[insurance_df.smoker=="yes"].charges)
y=np.array(insurance_df[insurance_df.smoker=="no"].charges)
t,p_value=st.ttest_ind(x,y,axis=0)
if (p_value<0.05):
  print(ha)
  print(p_value)
else:
  print(h0)
  print(p_value)

h0="bmi of males and females are the same "
ha="bmi of males and non females are not the same"
x=np.array(insurance_df[insurance_df.sex=="female"].bmi)
y=np.array(insurance_df[insurance_df.sex=="male"].bmi)
t,p_value=st.ttest_ind(x,y,axis=0)
if (p_value<0.05):
  print(ha)
  print(p_value)
else:
  print(h0)
  print(p_value)

h0="Region has no effect on smoking habits "
ha="Region has effect on smoking habit"
ct=pd.crosstab(insurance_df.region,insurance_df.smoker)
chi,p_value,dof,expected=st.chi2_contingency(ct)
print(ct)
if (p_value<0.05):
  print(ha)
  print(p_value)
else:
  print(h0)
  print(p_value)

"""add ftest or other test you think is necessary"""