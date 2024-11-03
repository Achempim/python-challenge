# -*- coding: UTF-8 -*-
"""PyPoll Homework Starter File."""

# Import necessary modules
import csv
import os

# Files to load and output
file_to_load = os.path.join("Resources", "election_data.csv")  # Input file path
file_to_output = os.path.join("analysis", "election_analysis.txt")  # Output file path

# Initialize variables to track the election data
total_votes = 0
candidates = {}  # Dictionary to track candidate names and vote counts
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Open the CSV file and process it
with open(file_to_load) as election_data:
    reader = csv.reader(election_data)
    header = next(reader)  # Skip the header row

    # Loop through each row of the dataset and process it
    for row in reader:
        total_votes += 1  # Increment total votes

        candidate_name = row[2]  # Get the candidate's name

        # If candidate is not in the candidates dictionary, add them
        if candidate_name not in candidates:
            candidates[candidate_name] = 0
        # Add a vote to the candidate's count
        candidates[candidate_name] += 1

# Prepare to save the output
with open(file_to_output, "w") as txt_file:

    # Print and write the total vote count
    election_results = (
        f"Election Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes}\n"
        f"-------------------------\n"
    )
    print(election_results)
    txt_file.write(election_results)

    # Loop through candidates and calculate percentages
    for candidate_name, votes in candidates.items():
        vote_percentage = (votes / total_votes) * 100

        # Determine if this candidate is the winning candidate
        if votes > winning_count:
            winning_count = votes
            winning_percentage = vote_percentage
            winning_candidate = candidate_name

        # Print and write each candidate's vote count and percentage
        candidate_results = f"{candidate_name}: {vote_percentage:.3f}% ({votes})\n"
        print(candidate_results)
        txt_file.write(candidate_results)

    # Print and write the winning candidate summary
    winning_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"-------------------------\n"
    )
    print(winning_summary)
    txt_file.write(winning_summary)



    # Save the winning candidate summary to the text file
