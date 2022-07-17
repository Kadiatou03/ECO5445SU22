# -*- coding: utf-8 -*-
"""
Created on Wed Jul 13 01:50:40 2022

@author: kadiatou
"""
#                                 Part 3: Data Collection and rearrangement
import os 
import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sns
import numpy as np 


# The current directory
os.getcwd()
# Change to a new directory.
git_path = 'C:/Users/kadiatou/Documents/GitHub/ECO5445/'
os.chdir(git_path + 'Project/Data')

# Check that the change was successful.
os.getcwd()

# Bringing in the data
df = pd.read_csv("hmda_sw.csv", delimiter=',')


# The variables chosen are the applicant and co-applicant race( A-race, Co-race ),The two Debt-to-income 
# ratios ( Expenses/income ) and ( obligations/income )Mortgage credit history (Credit history), 
# self-employed (S-employed), marital status, and education.


# The composition of the sample shows intuitive details about the applicants that can help assess whether
# there was racial discrimination in the mortgage approval process. The sample tells
# the race of the applicants, their education level, their marital status,and moreover, whether they are 
# self-employed and . The sample also include applicants net worth, their debts obligations compared to their 
# income whether their credit history meets loan policy guidelines for approval. 


# Marital status could affect the stability of the household income. 
# Is Marital status a big factor? Marital status is a protected category under the Equal Credit Opportunity Act.
# As the number of dependents increases for any given level of income, the applicant is likely to have less income available to carry the loan.
#Age could be an indicator of future earnings potential, as the slope of the age-earnings profile changes over the average person's working life


#Renanming the variables
df.rename(columns= {'s7':'Action_taken','s6':'Loan_amount','s13':'A_race','s24a':'No_dependents','s45':'Expenses/income','s46': 'Obligations/income','s27a':'Self_employed', 's23a':'Marital_status', 'school':'Education','netw':'Net_worth','uria':'Unemployed_Prob','s50':'Appraised_value','s34':'Other_financing','s25a':'Years_employed'}, inplace=True)
df.columns



# Convert numerical data from the selection into categorical data
df['Action_taken']=pd.Categorical(df.Action_taken)
df['A_race']=pd.Categorical(df.A_race)
df['Marital_status']=pd.Categorical(df.Marital_status)


# Review: should I change marital status data in code?


#                                     Part 4: Summary statistics 

# Table with the variables selected: df1

df1 = df[['Action_taken','Loan_amount','A_race','No_dependents','Expenses/income','Obligations/income','Self_employed','Marital_status','Education','Net_worth','Unemployed_Prob','Appraised_value','Other_financing','Years_employed']]


# Summary statistics
Summary_statistics = df1.describe()

# Loan amount (in thousands)
# Appraised value (in thousands) 



# The summary statistics shows that on average, people request $139,135 loans from banks and other lending institutions. 
# The average debt to income is 25.53 for expenses over income and 33.08 for obligations over income meaning that average 
# applicants has 25.53 of monthly gross income that goes toward paying expenses and 33.08 towards obligations. The average
# number of dependents claimed by applicants is 0.7605 and The schools year for certain applicant is erroneous as 999999 
# is the highest number of years of education. Therefore, it would be difficult to accurately assess the mean. since 
# Self_employed is based on 2 variables, the mean  0.1164  indicate that there is 11.64% of chance of having a self employed applicant. The applicant and 
# coapplicant average combined net worth is $253.041. 


# Scatterplots:
    ,'Net_worth','Unemployed_Prob','Appraised_value','Other_financing','Years_employed'
Scatter_data = df[['Loan_amount','Expenses/income','Obligations/income','Education']]  
sns.pairplot(Scatter_data, corner = True)

# Histograms 

df1.hist()

#Frequency counts

#           Race codes                Marital status                           Action taken codes  
 
#           3 – Black                 M - Married                       1 – Loan originated 
#           5 – White                 U - Unmarried                     2 – Application approved but not accepted by applicant 
#                                     S - Separated                     3 – Application denied     

df1[['Action_taken' ,'A_race']].groupby('Action_taken').count() 
# group by marital status applicant race and the action taken
df1[['Marital_status', 'A_race']].groupby('Marital_status').count() 


#                                 Part 5: Approval Probability

                              
                                         
# The baseline probability of an individual being approved for a mortgage
df1[['Action taken' ,'A-race']].groupby('Action taken').count() 

ap1  = df1 [(df1['Action taken'] == 1)].count() 
ap2 = df1 [(df1['Action taken'] == 2)].count()
Loan_approved = ap1 + ap2
Loan_approved
# 2095 loans approved out of 2380 loans requested

Approval_prob = Loan_approved/ 2380
Approval_prob
# 0.88025
# The probability of an individual being approved for a mortgage is 88%

                                  
#                                     Part 6: Table


# Count of total Black applicants: B
B = df1 [(df1['A_race'] == 3)].count()
# 339

# Count of approved black applicants:B1
B1 = df1 [(df1['A_race'] == 3)]
B1[['Action_taken' ,'A_race']].groupby('Action_taken').count()
# A total of 243 with  233 Loan originated and 10 Applications approved but not accepted by applicant

#Count of total white applicants:w
W = df1 [(df1['A_race'] == 5)].count()       
# 2041

# Count of approved white applicants: W1
W1 = df1 [(df1['A_race'] == 5)]
W1[['Action_taken' ,'A_race']].groupby('Action_taken').count()
# A total of 1852 with  60 Loan originated and 189 Applications approved but not accepted by applicant

# Table showing approval and denial data:
data = {'Applicant Race': ['Black','White','Total'],'Approved': ['243', '1852','2095'],'Not Approved': ['96', '189','285'],'Total': ['339', '2041','2380']}
table= pd.DataFrame(data)
 

#                                Part 7: Probabilities

# P(Approved | White) is the number of white applicants approved divided by total white applicants
Pw = 1852 / 2041
Pw
# 0.9074
# P(Approved | White) = 90.74%
# 

# P(Not Approved Black) is the number of black applicants not approved divided by total black applicants
Pb = 96 / 339
Pb
# 0.2832
# P(Not Approved | Black) = 28.32%
