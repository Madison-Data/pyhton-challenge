# import dependencies
import csv
import os
import pandas as pd

# identify file path 
path = os.path.join("Resources/election_data.csv")
df = pd.read_csv("Resources/election_data.csv")
# print(df.columns) to test
# print(df.head()) to test

# variables
totalvotes = df["Ballot ID"].count()
candidatetotals = df["Candidate"].value_counts()

# test variables. Candidate totals shows the specific candidates and the number of votes associated with them
# print(candidatetotals)
# print (totalvotes)

# vote counter variables

CCSvotesnum = int(0)
DGvotesnum = int(0)
RADvotesnum = int(0)


with open(path) as csvfile:
    reader = csv.reader(csvfile, delimiter=",")
    csvheaders = next(reader)
    #print(csvheaders) -- to test


    for row in reader:
        if row[2] == "Charles Casper Stockham":
            CCSvotesnum += int(1)
        elif row[2] == "Diana DeGette":
            DGvotesnum += int(1)
        elif row[2] == "Raymon Anthony Doane":
            RADvotesnum += int(1)
            
    winner = max({"Diana DeGette": DGvotesnum, "Charles Casper Stockham": CCSvotesnum, "Raymon Anthony Doane": RADvotesnum})

   # Print the analyis
    print("-------------------------")
    print("Election Results")
    print("-------------------------")
    print("Total Votes: ", "{:,.0f}".format(totalvotes))
    print("-------------------------")
    print("Diana DeGette: ", "{:,.0f}".format(DGvotesnum),  " | ", "{:,.2f}".format((DGvotesnum/totalvotes)*100), "%")
    print("Charles Casper Stockham: ", "{:,.0f}".format(CCSvotesnum), " | ", "{:,.2f}".format((CCSvotesnum/totalvotes)*100), "%")
    print("Raymon Anthony Doane: ", "{:,.0f}".format(RADvotesnum),  " | ", "{:,.2f}".format((RADvotesnum/totalvotes)*100), "%")
    print("-------------------------")
    print("Winner: ", winner)
    
with open("PyPollResults.txt", "w") as file:
    pypollresults = ("-------------------------\n","Election Results\n", "-------------------------\n","Total Votes: ", "{:,.0f}\n".format(totalvotes), "-------------------------\n", "Diana DeGette: ", "{:,.0f}".format(DGvotesnum),  " | ", "{:,.2f}".format((DGvotesnum/totalvotes)*100), "%\n","Charles Casper Stockham: ", "{:,.0f}".format(CCSvotesnum), " | ", "{:,.2f}".format((CCSvotesnum/totalvotes)*100), "%\n", "Raymon Anthony Doane: ", "{:,.0f}".format(RADvotesnum),  " | ", "{:,.2f}".format((RADvotesnum/totalvotes)*100), "%\n","-------------------------\n","Winner: ", winner, "\n", "Note: Diana DeGette is the actual winner. I do not know why the max function returns the lowest vote count. I think it might be because this is the last person in the dataset, as currently sorted, and the max function is somehow pulling the the maximum row instead of the maximum value computed earlier.")
    file.writelines(pypollresults)
    file.close()
