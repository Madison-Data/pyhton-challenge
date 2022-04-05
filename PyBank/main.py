# import dependcies
import csv
import pandas as pd
import os
import numpy as np

# filepath to csv file
budgetcsv = os.path.join("Resources/budget_data.csv")
# budgetcsv = pd.read_csv("Resources/budget_data.csv")
# print(budgetcsv)

# declare variables
rowcount = 0
totalnp = int()
pd.options.display.float_format = '${:,.0f}'.format

df = pd.read_csv("Resources/budget_data.csv")
# print(df.info)
# print(df.shape)
# print(df.describe)
# print(df.dtypes)
    # output: Date              object
            # Profit/Losses      int64


# open csv
with open(budgetcsv, encoding="UTF-8") as csvfile:
    reader = csv.reader(csvfile, delimiter=",")
    
    # print reader (to test)
    # print(reader)
    # ---

    # header
    csvheader = next(reader)
    # print header and data type
    # print(csvheader[0], ": ",type(budgetcsv), " | ", csvheader[1], ": ", type(budgetcsv))
    # output: ['Date': <cls str> , 'Profit/Losses' <cls str>]
    # ---

    # Count the rows in the file. Each row is one month
    for row in reader:
       rowcount+= int(1)  
    # print(rowcount, " rows")
    # output: 86.0 rows
    # --- 
  
    for row in reader:
            for i in line:
                    if i.isdigit()== True:
                        totalnp += int(1)
        # output: $22,564,198. 
                        #print(totalnp) to test

    avgnp = df.mean()
    maxprofit = df.max()
    minprofit = df.min()
    totalnp = int(rowcount*avgnp)
    #print(df.mean())
    #print(df.max)

    # Print the analysis statement
    print("-------------------------")
    print("Financial Analysis")
    print("-------------------------")
    print("Total Months: ", rowcount)
    print(f"Total Net Profits: ", "${:,.0f}".format(totalnp))
        # ${:,0f} formats the output as currency. No decimals
    print("Average Monthly Net Profit Change: ",avgnp)
    print("Greatest Increase in Profits: ", maxprofit)
    print("Greatest Decrease in Profits: ", minprofit)

with open("PyBankResults.txt", "w") as file: 
    pybankresults = ("-------------------------\n","Financial Analysis\n", "-------------------------\n", "Total Months: ", str(rowcount),"\n", f"Total Net Profits: ", "${:,.0f}".format(totalnp),"\n", "Average Monthly Net Profit Change: ", str(avgnp),"\n", "Greated Increase in Profits: ", str(maxprofit),"\n", "Greatest Decrease in Profits: ", str(minprofit), "\n")
    file.writelines(pybankresults)
    file.close()
