
# coding: utf-8

# # Task Option: Compute and Evaluate Models for All Possible Subsets

# In[1]:

import pandas as pd
import numpy as np
from sklearn import linear_model

# Read X,Y traces into pandas DataFrames named X,Y
X = pd.read_csv('X.csv')
Y = pd.read_csv('Y.csv')
# Create a single frame with selected columns
XY = pd.concat([X[['TimeStamp','all_..idle','X..memused', 'proc.s','cswch.s','file.nr','sum_intr.s','ldavg.1','tcpsck','pgfree.s']], Y['DispFrames']],axis=1)
# Change the format of time expression
timeIndex=pd.to_datetime(XY['TimeStamp'], unit='s')
XY.index=timeIndex
XY.head()


# In[2]:

# Split XY into training set and test set of set fraction size
from sklearn.model_selection import train_test_split
#Split data into random train and test subsets
train, test = train_test_split(XY, test_size = 0.3)
# Sort the train and test sets after index (which became unsorted through sampling)
train = train.sort_index(axis=0)
test = test.sort_index(axis=0)

# Get the columns label of XY dataset
List = list(XY)
List


# ## With the binary number from (1, 2^9) as flag to traverse all possible feature combinations

# In[3]:

# Computing and evaluating linear model for all possible sebsets
NAME = pd.DataFrame(index=range(2 ** 9),columns=['NAME'])
Y_train = train['DispFrames']; Y_test = test['DispFrames']

# With the binary number as the flag ,traverse all possible combination of attributes
for j in range(1,2 ** 9):
    X_train = pd.DataFrame(); X_test = pd.DataFrame()
    # Change the number to binary number
    i = bin(j)
    
    # Get the training and test subset
    for n in range(1,len(i)-1):
        a = int(i[-n])
        if a == 1:
            X_train[List[-n-1]] = train[List[-n-1]]
            X_test[List[-n-1]] = test[List[-n-1]]
        else:
            continue 
    
    # Create linear regression object, train and estimate the model
    regr = linear_model.LinearRegression()
    regr.fit(X_train, Y_train)
    name = np.mean(np.absolute(Y_test - regr.predict(X_test) ) )/ np.mean(Y_test)
    # Add the NAME value to the dataframe NAME
    NAME.iloc[j,0] = name
    
    
NAME.head()


# In[4]:

# Sort the data by the NAME values, get the best attributes comnbination
NAME.sort_values('NAME').head()


# In[5]:

import matplotlib.pyplot as plt
NAME['NAME'].hist(bins =  np.arange(0.1,0.3,0.01))
plt.title('The Histogram for NAME of Different Features Combinations_9 Features')
plt.xlabel('NAME Value')
plt.ylabel('Frequence')
plt.savefig('The Histogram for NAME of Different Features Combinations_9 Features.png')
plt.show()


# In[6]:

def count_1(a):
    count = 0
    while a != 0:
        if a % 2 == 1:
            count += 1
        a = a // 2
    return count


# In[7]:

N_1 = [];N_2 = [];N_3 = [];N_4 = [];N_5 = [];N_6 = [];N_7 = [];N_8 = [];N_9 = []
n1 = 1; n2 = 1;n3 = 1;n4 = 1;n5 = 1;n6 = 1;n7 = 1;n8 = 1;n9 = 1;
for i in range(1, 2**9):
    count = count_1(i)
    if count == 1:
        N_1.append(NAME.iloc[i,0])
        if NAME.iloc[i,0] < n1:
            n1 = NAME.iloc[i,0]
            flag1 = i
    elif count == 2:
        N_2.append(NAME.iloc[i,0])
        if NAME.iloc[i,0] < n2:
            n2 = NAME.iloc[i,0]
            flag2 = i
    elif count == 3:
        N_3.append(NAME.iloc[i,0])
        if NAME.iloc[i,0] < n3:
            n3 = NAME.iloc[i,0]
            flag3 = i
    elif count == 4:
        N_4.append(NAME.iloc[i,0])
        if NAME.iloc[i,0] < n4:
            n4 = NAME.iloc[i,0]
            flag4 = i
    elif count == 5:
        N_5.append(NAME.iloc[i,0])
        if NAME.iloc[i,0] < n5:
            n5 = NAME.iloc[i,0]
            flag5 = i
    elif count == 6:
        N_6.append(NAME.iloc[i,0])
        if NAME.iloc[i,0] < n6:
            n6 = NAME.iloc[i,0]
            flag6 = i
    elif count == 7:
        N_7.append(NAME.iloc[i,0])
        if NAME.iloc[i,0] < n7:
            n7 = NAME.iloc[i,0]
            flag7 = i
    elif count == 8:
        N_8.append(NAME.iloc[i,0])
        if NAME.iloc[i,0] < n8:
            n8 = NAME.iloc[i,0]
            flag8 = i
    elif count == 9:
        N_9.append(NAME.iloc[i,0])
        if NAME.iloc[i,0] < n9:
            n9 = NAME.iloc[i,0]
            flag9 = i


# In[8]:

print('The smallest NAME in 1 feature:'+ str(round(n1,4))+ '\n'+str(flag1)+
     '\nThe smallest NAME in 2 features:'+ str(round(n2,4))+ '\n'+str(flag2)+
     '\nThe smallest NAME in 3 features:'+ str(round(n3,4))+ '\n'+str(flag3)+
     '\nThe smallest NAME in 4 features:'+ str(round(n4,4))+ '\n'+str(flag4)+
     '\nThe smallest NAME in 5 features:'+ str(round(n5,4))+ '\n'+str(flag5)+
     '\nThe smallest NAME in 6 features:'+ str(round(n6,4))+ '\n'+str(flag6)+
     '\nThe smallest NAME in 7 features:'+ str(round(n7,4))+ '\n'+str(flag7)+
     '\nThe smallest NAME in 8 features:'+ str(round(n8,5))+ '\n'+str(flag8)+
     '\nThe NAME for 9 features:'+ str(round(n9,5)))


# In[10]:

plt.boxplot([N_1,N_2,N_3,N_4,N_5,N_6,N_7,N_8,N_9])
plt.title('The Boxplot for the Subsets of Size 1 to 9')
plt.xlabel('The Number of Subsets Features')
plt.ylabel('NAME Value')
plt.savefig('The Boxplot for the Subsets of Size 1 to 9.png')
plt.show()

