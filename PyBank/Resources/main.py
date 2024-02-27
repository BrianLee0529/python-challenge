import os
import csv

#Create list of data sort
#date = []
#Total = []

#variables
Total_Months= 0
Total_Profits= 0
Change_Profits= 0
greatest_Increase= 0
greatest_Decrease= 0

budget_csv = os.path.join('budget_data.csv')

#open csv file
with open(budget_csv) as csvfile:
    csvreader = csv.reader(csvfile,delimiter=',')
    csv_header = next(csvreader)
    data = list(csvreader)
    #print (data)
    #[['Jan-17', '607208'], 
    # ['Feb-10', '-354534'], 
    # ['Mar-10', '276622'], .....]

#['Date','Profit/Losses']

# print title Financial Analysis
print("Financial Analysis")

print("----------------------------")

# range(86) ======= [0, 1, 2, 3, ..... 85]
for i in range (86):
    # i=2
    # Total_Months=2
    Total_Months= Total_Months + 1
    # Total_Months=2 + 1
    row=data[i]
    #                0          1
    # row ====== ['Mar-17', '276622']
    one_profit_loss=row[1]
    # one_profit_loss======'276622'
    Total_Profits=Total_Profits + int(one_profit_loss)
    # Total_Profits='252674' + '276622'
#   print(row)

print("Total Month: " , Total_Months)

print("Total:" , Total_Profits)

# print("Average Change:" + )

# print("Greatest Increase in Profits:" + + )

# print("Greatest Decrease in Profits:" + + )