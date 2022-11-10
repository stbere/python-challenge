import os
import csv

# File path location
data = 'Resources/budget_data.csv'
my_report = open('Analysis/Budget_Analysis.txt', 'w')

with open(data) as strData:
    csvData = csv.DictReader(strData)

    months = 0
    total = 0
    total_ch = 0
    prev_rev = 1088983
    inc = ['',0]
    dec = ['',0]

    for row in csvData:
        months += 1
        rev = int(row['Profit/Losses'])
        total += rev
        change = rev - prev_rev
        total_ch += change
        prev_rev = rev

        if inc[1] < change:
            inc[0] = row['Date']
            inc[1] = change

        if dec[1] > change:
            dec[0] = row['Date']
            dec[1] = change

output = f'''
    Financial Analysis
  ----------------------------
  Total Months: {months}
  Total: ${total:,.2f}
  Average Change: ${total_ch/(months-1):,.2f}
  Greatest Increase in Profits: {inc[0]} (${inc[1]:,.2f})
  Greatest Decrease in Profits: {dec[0]} (${dec[1]:,.2f})'''

print(output)
my_report.write(output)