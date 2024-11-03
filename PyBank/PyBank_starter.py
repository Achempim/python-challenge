# -*- coding: UTF-8 -*-
"""PyBank Homework Starter File."""

# Dependencies
import csv
import os

# Files to load and output (update with correct file paths)
file_to_load = os.path.join("Resources", "budget_data.csv")  # Input file path
file_to_output = os.path.join("analysis", "budget_analysis.txt")  # Output file path

# Define variables
total_months = 0
total_net = 0
changes = []  # List to store monthly changes in "Profit/Losses"
previous_profit_loss = None  # To hold the value of "Profit/Losses" from the previous row
greatest_increase = {"date": "", "amount": float("-inf")}
greatest_decrease = {"date": "", "amount": float("inf")}

# Open and read the csv
with open(file_to_load) as financial_data:
    reader = csv.reader(financial_data)
    header = next(reader)  # Skip header

    # Extract first row to avoid appending to net_change_list
    first_row = next(reader)
    total_months += 1
    total_net += int(first_row[1])
    previous_profit_loss = int(first_row[1])  # Set initial value for comparison

    # Process each subsequent row
    for row in reader:
        total_months += 1
        current_profit_loss = int(row[1])
        total_net += current_profit_loss

        # Calculate the monthly change and update previous
        change = current_profit_loss - previous_profit_loss
        changes.append(change)
        previous_profit_loss = current_profit_loss

        # Check for greatest increase/decrease
        if change > greatest_increase["amount"]:
            greatest_increase = {"date": row[0], "amount": change}
        if change < greatest_decrease["amount"]:
            greatest_decrease = {"date": row[0], "amount": change}

# Calculate the average change
average_change = sum(changes) / len(changes)

# Generate the output summary
output = (
    f"Financial Analysis\n"
    f"----------------------------\n"
    f"Total Months: {total_months}\n"
    f"Total: ${total_net}\n"
    f"Average Change: ${average_change:.2f}\n"
    f"Greatest Increase in Profits: {greatest_increase['date']} (${greatest_increase['amount']})\n"
    f"Greatest Decrease in Profits: {greatest_decrease['date']} (${greatest_decrease['amount']})\n"
)

# Print the output
print(output)

# Write the results to a text file
with open(file_to_output, "w") as txt_file:
    txt_file.write(output)
