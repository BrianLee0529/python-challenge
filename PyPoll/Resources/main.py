import os
import csv

Election_csv = os.path.join('..','PyPoll','Resources','Election_data.csv')

#variables
Total_Votes = 0
Percentage_vote_Per_candidate = 0
Total_Number_vote_Per_candidate = 0

#Create list of data sort
Ballot ID= []
County = []
Candidate = []

with open(Election_csv) as csvfile
    csvreader = csv.reader(csvfile.delimiter=',')
    csv_header = next(csvreader)
    data = list(csvreader)
    # print title 
    Print("Electrion Results")
    Print("----------------------------")
    Print("Total Votes:")
    Print("----------------------------")
    
    
    
    
    Print("----------------------------")

    
    print (data)