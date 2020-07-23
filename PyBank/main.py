# Modules
import os
import csv

# Set path for file
csvpath = os.path.join("Resources", "budget_data.csv")

# Header
print("Financial Analysis")
print("-----------------------")

# Open the CSV
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    #print(csvreader)
    csv_header = next(csvreader)
    #print(f"CSV Header: {csv_header}")

    # The total number of months included in the dataset
    # The net total amount of "Profit/Losses" over the entire period
    month = []
    profit_losses = []
    for row in csvreader: 
        month.append(row[0])
        profit_losses.append(int(row[1]))
    print("Total Months: " + str(len(month)))
    print(f"Net Total Profit/Losses: {sum(profit_losses)}")


    # The average of the changes in "Profit/Losses" over the entire period
    monthly_change = []
    for i in range(len(profit_losses) -1):
        monthly_change.append(profit_losses[i+1]-profit_losses[i])
        average_change = sum(monthly_change)/len(monthly_change)
    print(f"Average Changes: {round(average_change, 2)}")


    # The greatest increase in profits (date and amount) over the entire period
    max_increase = max(monthly_change)
    #print(month[max_index + 1])
    increase_index = monthly_change.index(max_increase)
    #print(increase_index)
    print(f"Greatest Increase in Profits: {month[increase_index + 1]} (${max_increase})")
    

    # The greatest decrease in losses (date and amount) over the entire period
    max_decrease = min(monthly_change)
    #print(max_decrease)
    decrease_index = monthly_change.index(max_decrease)
    #print(decrease_index)
    print(f"Greatest Decrease in Profits: {month[decrease_index + 1]} (${max_decrease})")

    