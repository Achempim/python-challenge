import csv

# File path to your CSV file
file_path = "C:/Users/HP/Desktop/python-challenge/PyBank/Resources/budget_data.csv"

# Initialize variables
total_months = 0
net_total = 0
previous_profit_loss = None
changes = []
months = []

# Read the CSV file
with open(file_path, mode='r') as file:
    csvreader = csv.reader(file)
    header = next(csvreader)  # Skip the header row

    for row in csvreader:
        # Extract date and profit/loss
        date = row[0]
        profit_loss = int(row[1])

        # Count the total number of months
        total_months += 1

        # Calculate the net total amount of Profit/Losses
        net_total += profit_loss

        # Calculate the changes in Profit/Losses
        if previous_profit_loss is not None:
            change = profit_loss - previous_profit_loss
            changes.append(change)
            months.append(date)

        previous_profit_loss = profit_loss

# Calculate the average change
average_change = sum(changes) / len(changes)

# Find the greatest increase and decrease in profits
max_increase = max(changes)
max_decrease = min(changes)
max_increase_month = months[changes.index(max_increase)]
max_decrease_month = months[changes.index(max_decrease)]

# Print the results
print("Financial Analysis")
print("---------------------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${net_total}")
print(f"Average Change: ${average_change:.2f}")
print(f"Greatest Increase in Profits: {max_increase_month} (${max_increase:.0f})")
print(f"Greatest Decrease in Profits: {max_decrease_month} (${max_decrease:.0f})")
