# Add our dependencies.
import csv
import os
# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")

# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Open the election results and read the file.
total_votes = 0
candidate_options = []
#declare an empty dictionary to carry candidate names and their total count 
candidate_votes = {}
winning_count = 0
winning_percentage = 0
winning_candidate = ""

with open(file_to_load) as election_data:

    file_reader = csv.reader(election_data)
    # To do: read and analyze the data here
    #for row in file_reader:
    header_rows = next(file_reader)

    for row in file_reader:
        #print(row)
        total_votes +=1
        candidate_name = row[2]
        if candidate_name not in candidate_options:
            candidate_votes[candidate_name] = 0
            candidate_options.append(candidate_name)
        candidate_votes[candidate_name] += 1

for candidate in candidate_options:
    votes = candidate_votes[candidate]
    vote_percentage = float(votes) / float(total_votes) * 100
    #print(f"{candidate}: recieved {round(vote_percentage, 2)}% of the vote")
    if votes > winning_count:
        winning_count = votes
        winning_candidate = f"the winning candidate is {candidate} with {votes} votes and winning at {round(vote_percentage,2)}%"
        

print(winning_candidate)

#print(total_votes)
#print(candidate_votes)

