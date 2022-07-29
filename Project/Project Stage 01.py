###############################################################################
# Copy header formatting from my scripts
# Script fails to fully run
###############################################################################

# Part 3: Data Collection and rearrangement
import os 
import pandas as pd 
# import matplotlib.pyplot as plt was imported, but not used
import seaborn as sns


# The current directory
os.getcwd()
# Change to a new directory.
git_path = 'C:/Users/kadiatou/Documents/GitHub/ECO5445/'
git_path = 'C:/Users/jo585802/OneDrive - University of Central Florida/Documents/GitHub/ECO5445/' # Needed line to test data
os.chdir(git_path + 'Project/Data')

# Check that the change was successful.
os.getcwd()

# Bringing in the data
df = pd.read_csv("hmda_sw.csv", delimiter=',')

# Choice of variables

# The composition of the sample shows intuitive details that can help assess whether there was racial discrimination in the mortgage
# approval process. The variables chosen are the applicants race (A_race) to test the main hypothesis, their monthly income (Monthly_income), 
# the two Debt-to-income ratios ( Expenses/income ) and ( obligations/income ) that shows applicant's debts obligations compared to their income
# and applicants'ability to pay back a loan, their marital status(Marital_status) which could affect the stability of the household income, as well 
# as their level of education (Education) which can approximate their earnings and allows speculations about their credit worthiness. 
 
# The sample also tells whether applicants are self-employed (Self_employed) because self-employed individuals tend to suffer more income risk and
# their earnings are more difficult to verify. The sample accounts for the Applicants'probability of unemployment (Unemployed_Prob) which is also important
# because lenders are skeptical about individuals who are employed in depressed sectors of regional economy, as well as the number of years employed in 
# applicable line of work (Years_employed) as a strong employment history proves the applicant has a steady income and ability to make regular loan payments.

# The sample further includes variables such as the number of dependents('No_dependents') which can affect the income available to carry the loan, the 
# type of action taken (Action_taken) by lenders, the Loan amount requested by applicants (Loan_amount), the applicants'credit history:(MTG_credit_history) 
# and (Consum_credit_hist) because the more severe applicant's past credit problems are, the higher the probability that their loans are denied, and the 
# Futhermore, the sample has applicants' liquid assets in dollaranounts which can be easily trade for cash within a short amount of time to pay mortgage 
# if necesssary. Finally, the selection contains information about the Appraised value of the house (Appraised_value) which ensures that applicants are not 
# entering into a bad real estate deal, and the appraisal also directly affects the amount of mortgage loaned.
 

#Renanming the variables
df.rename(columns= {'s7':'Action_taken','s6':'Loan_amount','s13':'A_race','s24a':'No_dependents','s25a':'Years_employed','s45':'Expenses/income','s46': 'Obligations/income','s27a':'Self_employed', 's23a':'Marital_status', 'school':'Education','s31a':'Monthly_income','s35':'Liquid_assets','s50':'Appraised_value','uria':'Unemployed_Prob', 's42':'MTG_credit_hist', 's43':'Consum_credit_hist'}, inplace=True)
df.columns


# Convert numerical data from the selection into categorical data
df['Action_taken']=pd.Categorical(df.Action_taken)
df['A_race']=pd.Categorical(df.A_race)
df['Marital_status']=pd.Categorical(df.Marital_status)
df['No_dependents']=pd.Categorical(df.No_dependents)
df['MTG_credit_hist']=pd.Categorical(df.MTG_credit_hist)
df['Consum_credit_hist']=pd.Categorical(df.Consum_credit_hist)

# Hypotheses

# Given the sample, the following hypotheses are build on the quantitative variable and relationship direction is indicated by (+) and (-)

# H1: The higher the appraisal value, the higher the loan amount (loan is based on the apparaisal) (+)
# H2: The higher the monthly income, the higher loan amount, (individuals would not borrowed beyond what they can afford to pay back) (+)
# H3: The higher the loan amount, the lower the two Debt-to-income ratios, (showing ability to pay) (-) 
# H4: The higher the number of dependents, the higher Expenses/income (showing effect of dependent on debt to income ratio) (+)
# H5: The higher the number of years of education, the higher employment years (More educated individuals tend to be stable on the job market) (+)
# H6: The higher the monthly income, the lower the two Debt-to-income ratios (Displaying ability to pay back loan) (-)
# H7: The higher the number of years of education, the lower the probabilty of being unemployed (More educated individuals have low unemployment probability) (-)
# H8: The higher the number of years of education, the higher the monthly income (+)

#                                                           Part 4: Summary statistics 

# Table with the variables selected: df1

###############################################################################
# Didn't happen to notice that 999,999.4 is the designation for missing 
# numerical data. Summary statistics will be skewed.
###############################################################################

df1 = df[['Action_taken','Loan_amount','A_race','No_dependents','Years_employed','Expenses/income','Obligations/income','Self_employed','Marital_status','Education','Unemployed_Prob','Appraised_value','Monthly_income', 'Liquid_assets','MTG_credit_hist', 'Consum_credit_hist']]


# Summary statistics
Summary_statistics = df1.describe()
# Loan amount (in thousands)
# Appraised value (in thousands) 


# The summary statistics shows that on average, applicants request around $139,135 from banks and other lending institutions to finance their house purchase. 
# for this variable, the high standard deviation indicates that the data for loan amount are spread out. The average debt to income is 25.53 for expenses over
# income and 33.08 for obligations over income meaning that average applicant has 25.53 of monthly gross income that goes toward paying expenses and 33.08 
# towards paying obligations. The standard deviation of the ratios are similar and show that the data are slighlty clustered around the mean. Since Self_employed
# is based on 2 outcomes, the mean  0.1164 indicate that there is 11.64% of chance of having a self employed applicant. The average of the different probabilities
# of unemployment by industry is 3% with a standard deviation of 2.02 meaning that the data are clustered around the mean. The average apraisail value of houses is 
# $198,543 and the high standard deviation tells that the data are not grouped close to the mean.The average applicant has $4914.02 of monthly income. The average
# the standard deviation here is the highest given the data type. On the other hand, the average as well as the standard deviation of the numbers of years being
# employed in applicable line of work, the number of school year of applicants and the amounts of liquid assets are erroneous as they contains the number '999999' 
# that was used in the database to indicate missing observations. Therefore, it would be difficult to accurately assess them. 


# Some interesting Correlation between variables testing the hypotheses

hypothesis1_data = df[["Appraised_value","Loan_amount"]]
test_hypothesis1_data= hypothesis1_data.corr()
test_hypothesis1_data.iloc[0,1]
# Corr = 0.72674, as predicted, there is a positive relationship between the variables and  it is quite strong. 
# High loan amounts should be backed by an appropriate appraisal value


hypothesis2_data = df[["Monthly_income","Loan_amount"]]
test_hypothesis2_data= hypothesis2_data.corr()
test_hypothesis2_data.iloc[0,1]
# Corr = 0.57994, as predicted, there is a positive relationship between the variables that is fairly strong.
# The monthly should be enough to cover the loan amount


hypothesis3a_data = df[["Loan_amount","Expenses/income"]]
test_hypothesis3a_data= hypothesis3a_data.corr()
test_hypothesis3a_data.iloc[0,1]
# Corr = 0.06986, does not agree with the H3. There is a very weak relationship between the variables which indicates
# that they may not be correlated. Therefore, the debt ratio does not influcence the loan amount.

hypothesis3b_data = df[["Loan_amount","Obligations/income"]]
test_hypothesis3b_data= hypothesis3b_data.corr()
test_hypothesis3b_data.iloc[0,1]
# Corr = 0.062999, similarly, this does not agree with H3. There is a very weak relationship between the variables 
# which indicates that they may not be correlated. Therefore, the debt ratio does not influcence the loan amount.

hypothesis4_data = df[["No_dependents","Expenses/income"]]
test_hypothesis4_data= hypothesis4_data.corr()

###############################################################################
# Had to comment this next line out, this is not a 2x2 matrix
###############################################################################
# test_hypothesis4_data.iloc[0,1]

# Corr = 0.024701, this extremely weak correlation does not agree with H4 and may indicate that the number of dependent
# do not have a significant effect on the debt ratio (Expenses/income)

hypothesis5_data = df[["Education","Years_employed"]]
test_hypothesis5_data= hypothesis5_data.corr()
test_hypothesis5_data.iloc[0,1]
# Corr = 0.202061. H5 is weakly proven by this correlation but there is a slightly moderate and positive relationship 
# between the number of years being employed and the level of education.

hypothesis6a_data = df[["Monthly_income","Expenses/income"]]
test_hypothesis6a_data= hypothesis6a_data.corr()
test_hypothesis6a_data.iloc[0,1]
# Corr = -0.221467, as predicted, it is negative relationship and the variables are inversely correlated. Nonetheless, 
# it is still a weak correlation meaning that as monthly income increases, expenses/income ratio slightly decreases.

hypothesis6b_data = df[["Monthly_income","Obligations/income"]]
test_hypothesis6b_data= hypothesis6b_data.corr()
test_hypothesis6b_data.iloc[0,1]
# Corr = - 0.163608, as predicted, H6 is weakly proven as the negative coefficient indicates that the two variables are 
# negatively correlated, therefore, as monthly income increases, Obligations/income ratio slightly decreases

hypothesis7_data = df[["Education","Unemployed_Prob"]]
test_hypothesis7_data= hypothesis7_data.corr()
test_hypothesis7_data.iloc[0,1]
# Corr = 0.011410, the coefficient is positive but so low, that there may be not a relationship between the level of education
# and the numbers of years being employed. Therefore, H7 is not proven.

hypothesis8_data = df[["Education","Monthly_income"]]
test_hypothesis8_data= hypothesis8_data.corr()
test_hypothesis8_data.iloc[0,1]
# Corr = -0.0033949, H8 predicted a positive relationship but the coefficient says the contrary. Nonetheless, it is such a 
# low number that it can be implied that there is no relationship between the level of education and monthly income.

# Scatterplots:
    
# The relationship between the different variables will be shown by the scatterplots. p

# The variables are grouped by their hypothesized relationship

Scatter_data1 = df[['Loan_amount','Appraised_value','Expenses/income','Obligations/income','Monthly_income']] 
sns.pairplot(Scatter_data1, corner = True)

###############################################################################
# This plot fails to compile
###############################################################################
Scatter_data2 = df[['Monthly_income','Liquid_assets','No_dependents','Years_employed','Years_employed']] 
sns.pairplot(Scatter_data2, corner = True)

# The plots provide a better illustration of some correlationsor non-correlation found above. For instance, H1 that  
# states that there is positive relationship betweem appraisal value and loan amount is visible and we can se why H3 
# is weakly asset as the differents points shows almost a horizontal line. 


# Histograms 

# A more intuitive representation of the dataset is depicted by the differents histograms. They show the frequency distribution 
# of the data set and the most common outcome of the variables selected.

HistogramData = df[['Loan_amount','No_dependents','Years_employed','Expenses/income','Obligations/income','Education','Unemployed_Prob','Appraised_value','Monthly_income', 'Liquid_assets']]
HistogramData.hist()

# For each variable, the distribution is observable as expressed by the standard deviation and we can see the outlier'999999' for the
# numbers of years being employed in applicable line of work, the number of school year of applicants and the amounts of liquid assets
# are erroneous as they contains the number 


# Frequency counts and Pie Charts for qualitative variables

#  Race codes   Marital status       Action taken codes                   Consumer Credit History                  Mortgage Credit History
                        
#  3 – Black     M - Married      1 – Loan originated                      1 – No late mortgage payments               1 - No "slow pay" or delinquent accounts, but
#  5 – White     U - Unmarried    2 – Application approved, not accepted   2 – No mortgage payment history                sufficient references for determination
#                S - Separated    3 – Application denied                   3 - One or two late mortgage payments       2 - One or two "slow pay" account(s) (each with 
#                                                                          4 – More than two late mortgage payments        one or two payments 30 days past due) 
#                                                                                                                      3- More than two "slow pay" accounts (each with one or two payments 
#                                                                                                                         30 days past due); or one or two chronic "slow pay" account(s) (with 
#                                                                                                                         three or more payments 30 days past due in any 12-month period) 
#                                                                                                                     4 – Insufficient credit history or references for determination 
#                                                                                                                     5 – Delinquent credit history (containing account(s) with a history of 
#                                                                                                                         payments 60 days past due)
#                                                                                                                     6 – Serious delinquencies (containing account(s) with a history of 
#                                                                                                                         payments 90 days past due) 

MaritalStatus = df['Marital_status'].value_counts()
MaritalStatus.plot.pie(autopct='%1.1f%%',subplots=True)

ActionTaken = df['Action_taken'].value_counts()
ActionTaken.plot.pie(autopct='%1.1f%%',subplots=True)

ApplicantRace = df['A_race'].value_counts()
ApplicantRace.plot.pie(autopct='%1.1f%%',subplots=True)

MortgageCreditHistory = df['MTG_credit_hist'].value_counts()
MortgageCreditHistory.plot.pie(pctdistance=1.5,autopct='%1.1f%%', subplots=True)

ConsumerCreditHistory = df['Consum_credit_hist'].value_counts()
ConsumerCreditHistory.plot.pie(autopct='%1.1f%%',subplots=True) 


###############################################################################
# What does this all say about the average applicant?
###############################################################################

#                                 Part 5: Approval Probability
                              
# The baseline probability of an individual being approved for a mortgage
df1[['Action_taken' ,'A_race']].groupby('Action_taken').count() 

App1  = df1 [(df1['Action_taken'] == 1)].count() # loan originated
App2 = df1 [(df1['Action_taken'] == 2)].count()  # Loan approved but not accepted by applicant
Loan_approved = App1 + App2
Loan_approved
# 2095 loans approved out of 2380 loans requested

Approval_prob = 2095 / 2380
Approval_prob
# 0.88025

# The probability of an individual being approved for a mortgage is 88%

                                  
#                                                                  Part 6: Table


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
ApplicantData = {'Applicant Race': ['Black','White','Total'],'Approved': ['243', '1852','2095'],'Not Approved': ['96', '189','285'],'Total': ['339', '2041','2380']}
Table= pd.DataFrame(ApplicantData)
 

#                                                      Part 7: Probabilities

###############################################################################
# This next part requires you to look at a table, then manually input values.
# We can extract values from the tables instead of hand typing them
###############################################################################

# P(Approved | White) is the number of white applicants approved divided by total white applicants
Pw = 1852 / 2041
Pw
# 0.9074
# P(Approved | White) = 90.74%
# 

# P(Not Approved | Black) is the number of black applicants not approved divided by total black applicants
Pb = 96 / 339
Pb
# 0.2832
# P(NotApproved | Black) = 28.32%

# From this calculation, it can be implied that white applicants have close to 20% more chance of being approved for mortgage loans than black applicants.
# Testing the correlation between some of the variables such as the monthly income and the two Debt-to-income ratios do not provide satisfying results given the
# circumstances. It appears that the variables are not being appropriately used regarding the loan approval requirements because it is logical to have a strong 
# negative correlation as they are factors that determine credit worthiness. Also, the relationship between Monthly income and the loan amount is not as positively 
# strong as it should. Futhermore,from the consumer credit history pie chart, we can see that 21.3% of applicants have a bad consumer credit history. In the paper,
# it was also mentioned that given the same property and personal characteristics, white applicants have the advantage of a general presumption of creditworthiness 
# and black applicants do not.This can explained by the fact that we have such a high approval rate while applicants'credit history do not macthed that performance.

# It is plausible to assume that there might be some racial discrimination in the process to discredit black applicants
