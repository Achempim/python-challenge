import csv
import os
os.chdir(r'C:\Users\HP\Desktop\Boot camp\Challenge\python-challenge\PyPoll')
current_path = os.path.join("Resources", "budget_data.csv")
print(os.path.abspath(current_path))
print("Current working directory:")
print(os.getcwd())

# File path to your CSV file
file_path = os.path.join("Resources", "election_data.csv")

print(file_path)

# Initialize variables
total_votes = 0
candidates = []
candidate_votes = {}

# Read the CSV file
with open(file_path, mode='r') as file:
    csvreader = csv.reader(file)
    header = next(csvreader)  # Skip the header row

    for row in csvreader:
        # Extract the candidate name from each row
        candidate = row[2]

        # Count the total number of votes
        total_votes += 1

        # Add candidate to the list if not already in it
        if candidate not in candidates:
            candidates.append(candidate)
            candidate_votes[candidate] = 0

        # Count votes for each candidate
        candidate_votes[candidate] += 1

# Calculate the percentage of votes each candidate won
candidate_percentages = {candidate: (votes / total_votes) * 100 for candidate, votes in candidate_votes.items()}

# Determine the winner of the election based on popular vote
winner = max(candidate_votes, key=candidate_votes.get)

# Print the results
print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------")
for candidate in candidates:
    print(f"{candidate}: {candidate_percentages[candidate]:.3f}% ({candidate_votes[candidate]})")
print("-------------------------")
print(f"Winner: {winner}")
print("-------------------------")
