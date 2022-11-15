import os
import csv

# File path location
data = 'PyPoll/Resources/election_data.csv'
my_report = open('PyPoll/Analysis/Election_Analysis.txt', 'w')

total_votes = 0
candidates=[]
candidate_votes={}
high_votes = 0
winner=" "

# Time to find some variables..correctly, i hope
with open(data) as strData:
    csvData = csv.DictReader(strData)
    # print(csvData)
    next(csvData)
    for rows in csvData:
        name=rows["Candidate"]
        if name not in candidates:
            candidates.append(name)
            candidate_votes[name]=1
        else:


            candidate_votes[name]+=1   
        total_votes+=1
    print(f"Election Results")
    print(f"Total Votes: {total_votes}")
    my_report.write(f"{total_votes}\n")
    for name in candidates:
        votes=candidate_votes.get(name)
        percentage =(votes/total_votes)* 100
        print(f"{name}:{round(percentage,2)}% ({votes}),\n")
        my_report.write(f"{name}:{round(percentage,2)}% ({votes}),\n")

print(f"Winner {max(candidate_votes, key=candidate_votes.get)}")
# output=f'''
# Election Results
# -------------------------
# Total Votes: {total_votes}
# {candidates}, {round(percentage,2)}% 
# -------------------------
# '''

'''
  Charles Casper Stockham: 23.049% (85213)
  Diana DeGette: 73.812% (272892)
  Raymon Anthony Doane: 3.139% (11606)
  -------------------------
  Winner: Diana DeGette
  -------------------------
  '''

# print(output)
# my_report.write(output)
