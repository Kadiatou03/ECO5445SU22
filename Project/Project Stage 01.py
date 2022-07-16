#                                 Part 3: Data Collection and rearrangement
import os 
import pandas as pd 

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


# The composition of the sample shows intuitive details about the applicants and co-applicants that can
# help assess whether there was racial discrimination in the mortgage approval process. The sample tells
# the race of the applicants, their education level, their marital status,and moreover, whether they are 
# self-employed. The sample also include applicants net worth, their debts obligations compared to their 
# income whether their credit history meets loan policy guidelines for approval. Finally, we have the 
# decisions of lenders and the reason for denial, in case loans are not approved


#Renanming the variables
df.rename(columns= {'s7':'Action taken','s13':'A-race','s14':'Co-race','s45':'Expenses/income', 's46': 'Obligations/income','s27a':'S-employed', 's23a': 'Marital status', 'school':'Education','netw':'Net worth','s44':'Public records', 's40':'Requirements met','s19a':'Denial R','s42':'Credit history'}, inplace=True)
df.columns


#                                     Part 4: Summary statistics 

# Table with the variables selected

df1 = df[['Action taken','A-race','Co-race','Expenses/income','Obligations/income','S-employed','Marital status', 'Education','Public records','Net worth','Requirements met','Denial R', 'Credit history']]

# summary statistics
i = df1.describe()
df1_median = df1.median()

# The summary statistics shows that the mean of the action taken by banks and other lending institutions 
# is 1.267 and which indicates that on average loan are most likely originated. The applicants and 
# co-applicants race are between 4 and close to 6 meaning that most applicants are either hispanic or 
# white. The average debt to income is 25.53 for expenses over income and 33.08 for obligations over 
# income meaning that average applicants has 25.53 of monthly gross income that goes toward paying 
# expenses and 33.08 towards obligations. The schools year for certain applicant is erroneous. Therefore,
# it would be difficult to accurately assess the mean. The average applicants are self employed, the 
# average net worth is $253.041. They have no late mortgage payments or no mortgage payment history. 
# Their credit history public records is either not considered or they have no public record defaults. 
# Therefore, the average applicants credit history meets loan policy guidelines for approval



# Is there a correlation between the acction taken and the race of the applicant?

#                    Race codes                     Action taken codes  
#  
# 1 – American Indian or Alaskan Native          1 – Loan originated 
# 2 – Asian or Pacific Islander                  2 – Application approved but not accepted by applicant 
# 3 – Black                                      3 – Application denied 
# 4 – Hispanic                                   4 – Application withdrawn 
# 5 – White                                      5 – File closed for incompleteness 
# 6 – Other                                      6 – Loan purchased by institution 
# 7 – Information not provided by applicant                  



df_subset = df[['Action taken','A-race']]
corr = df_subset.corr()
corr.iloc[0,1]
# -0.20178430394854543

# There is a weak inverse relationship between 'Action taken' and 'A-race'. This indicates that the higher
# race code, the lower the action taken codes. Therefore, according to this result, white applicants has a 
# slighty better chance of being approved


df_subset.plot.scatter(x ='Action taken', y='A-race')
df_subset.hist()

#                                    Part 5: Approval Probability

# The baseline probability of an individual being approved for a mortgage
df1[['Action taken' ,'A-race']].groupby('Action taken').count() # 

ap1  = df1 [(df1['Action taken'] == 1)].count() 
ap2 = df1 [(df1['Action taken'] == 2)].count()
Loan_approved = ap1 + ap2
Loan_approved
# 2095 loans approved out of 2380 loans requested

Approval_prob = 2095/2380
# 0.88025
# The probability of an individual being approved for a mortgage is 88%

                                      
#                                     Part 6: Table
df1[['Action taken' ,'A-race']].groupby('A-race').count() 
# Count of total Black applicants
B = df1 [(df1['A-race'] == 3)].count()
# 339

# Count of approved black applicants
B1 = df1 [(df1['A-race'] == 3)]
B1[['Action taken' ,'A-race']].groupby('Action taken').count()
# A total of 243 with  233 Loan originated and 10 Applications approved but not accepted by applicant

#Count of total white applicants
W = df1 [(df1['A-race'] == 5)].count()       
# 2041

# Count of approved white applicants
W1 = df1 [(df1['A-race'] == 5)]
W1[['Action taken' ,'A-race']].groupby('Action taken').count()
# A total of 1852 with  60 Loan originated and 189 Applications approved but not accepted by applicant

# Table showing approval: Calcul
data = {'Applicant Race': ['Black','White'],'Approved': ['243', '1852'],'Not Approved': ['96', '189']}
table= pd.DataFrame(data)
 
 
table.loc['Column_Total']= df.sum(numeric_only=True, axis=0)
table.loc[:,'Row_Total'] = df.sum(numeric_only=True, axis=1)

#                                Part 7: Probabilities

# P(Approved | White) is the number of white applicants approved divided by total applicants
Pw = 1852 / 2380
Pw

# P(Not Approved Black) is the number of black applicants approved divided by total applicants
Pb = 243 / 2380
Pb

