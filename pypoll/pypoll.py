# Import Modules

import csv
import os

# Create file path

file_to_load = os.path.join("pypoll", "Resources", "election_data.csv")

# Set Variables

total_votes = 0
candidates = []
vote_counts = []
percent_votes_won =[]
poll_results = {"count_vote": vote_counts, "percentages": percent_votes_won}  

# Open CSV

with open(file_to_load) as election_data:
    reader = csv.reader(election_data)

# Iterate over headers

    header = next(reader)

# Create a list of candidates

    for row in reader:

        total_votes += 1

        # Increment the vote count by 1 per candidate


        if row[2] not in candidates:
            candidates.append(row[2])
            vote_counts.append(1)

        else:
            vote_counts[candidates.index(row[2])] +=1
            
        # Create a new list of percentages

    for i in range(len(vote_counts)):
        percent_votes_won.append(round(((vote_counts[i]/total_votes)*100), 3))

        # Announce the winner
    winner =  '      '
    for i in range(len(candidates)):
        if poll_results["count_vote"][i] == max(poll_results["count_vote"]):
            winner = candidates[i]

# Print an analysis

print()
print(f'Election Results')
print(f'----------------')
print(f'Total Votes: {total_votes}')
print(f'-----------')
print(f'{candidates[0]}: {percent_votes_won[0]}, {vote_counts[0]}')
print(f'{candidates[1]}: {percent_votes_won[1]}, {vote_counts[1]}')
print(f'{candidates[2]}: {percent_votes_won[2]}, {vote_counts[2]}')
print(f'{candidates[3]}: {percent_votes_won[3]}, {vote_counts[3]}')

print(f'-----------')
print(f'Winner: {winner}')


import sys
sys.stdout = open('Pypoll_Output.txt', 'wt')

print(f'Election Results')
print(f'----------------')
print(f'Total Votes: {total_votes}')
print(f'----------------')
print(f'{candidates[0]}: {percent_votes_won[0]}, {vote_counts[0]}')
print(f'{candidates[1]}: {percent_votes_won[1]}, {vote_counts[1]}')
print(f'{candidates[2]}: {percent_votes_won[2]}, {vote_counts[2]}')
print(f'{candidates[3]}: {percent_votes_won[3]}, {vote_counts[3]}')

print(f'-----------------')
print(f'Winner: {winner}')
