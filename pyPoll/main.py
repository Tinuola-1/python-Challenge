import os
import csv
#Define variables

# Pull in data & read file
csvpath = os.path.join('Resources', 'election_data.csv')
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')
    next(csvreader)
    data = list(csvreader)
    row_count = len(data)
    #new list
    candidates = list()
    tally = list()
    for i in range (0,row_count):
        candidate = data[i][2]
        tally.append(candidate)
        if candidate not in candidates: 
            candidates.append(candidate)
    countcandi = len(candidates)

  # The total number of votes and percentage won by each candidate
    votes = list()
    percentage = list()
    for j in range (0,countcandi):
        name = candidates[j]
        votes.append(tally.count(name))
        votesprct = votes[j]/row_count
        percentage.append(votesprct)

  #  winner
    winner = votes.index(max(votes))    

#print output
    print("Election Results")
    print("----------------------------")
    print(f"Total Votes: {row_count:,}")
    print("----------------------------")
    for k in range (0,countcandi): 
        print(f"{candidates[k]}: {percentage[k]:.3%} ({votes[k]:,})")
    print("----------------------------")
    print(f"Winner: {candidates[winner]}")
    print("----------------------------")

  # Print output to "PyPoll.txt" file
    print("Election Results", file=open("PyPoll.txt", "a"))
    print("----------------------------", file=open("PyPoll.txt", "a"))
    print(f"Total Votes: {row_count:,}", file=open("PyPoll.txt", "a"))
    print("----------------------------", file=open("PyPoll.txt", "a"))
    for k in range (0,countcandi): 
        print(f"{candidates[k]}: {percentage[k]:.3%} ({votes[k]:,})", file=open("PyPoll.txt", "a"))
    print("----------------------------", file=open("PyPoll.txt", "a"))
    print(f"Winner: {candidates[winner]}", file=open("PyPoll.txt", "a"))
    print("----------------------------", file=open("PyPoll.txt", "a"))
