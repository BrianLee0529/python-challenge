import os
import csv

#Create list of data sort
#date = []
#Total = []

#variables
total_months= 0
total_profits= 0
change_profits= 0
greatest_increase= 0
greatest_decrease= 0

budget_csv = os.path.join('budget_data.csv')

#open csv file
with open(budget_csv) as csvfile:
    csvreader = csv.reader(csvfile,delimiter=',')
    csv_header = next(csvreader)
    data = list(csvreader)
    # print(data[0])
    #print (data)
    #[['Jan-17', '1088983'], 
    # ['Feb-10', '-354534'], 
    # ['Mar-10', '276622'], .....]

#['Date','Profit/Losses']

# print title Financial Analysis
print("Financial Analysis")

print("----------------------------")

changes = []
# [t_1-t_0, t_2-t_1, t_3-t_2, ...]

# range(86) ======= [0, 1, 2, 3, ..... 85]
for i in range(86):
    # print (i)
    # i=2
    # Total_Months=2
    total_months= total_months + 1
    # Total_Months=2 + 1
    row=data[i]
    # print(row[0])
    #                0          1
    # row ====== ['Mar-17', '276622']
    one_profit_loss=int(row[1])
    # one_profit_loss======'276622'
    total_profits = total_profits + one_profit_loss
    if i > 0 : 
        change = one_profit_loss - int(data[i-1][1])
        changes.append(change)
    # Total_Profits='252674' + '276622'
    #   print(row)
    if 


    
total_change = sum(changes)

print("Total Months: " + str(total_months))

print("Total:" , total_profits)

average_change =  total_change / (total_months-1)

print("Average Change:" + str(average_change))

# print("Greatest Increase in Profits:" + + )

# print("Greatest Decrease in Profits:" + + )