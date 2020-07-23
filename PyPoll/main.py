# Modules
import os
import csv

# Set path for file
csvpath = os.path.join("Resources", "election_data.csv")

# Prining Header
print("Election Results")
print("-----------------------")


# Open the CSV
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    #print(csvreader)
    csv_header = next(csvreader)
    #print(f"CSV Header: {csv_header}")

    # The total number of votes cast
    voters = []
    Otooley = []
    Correy = []
    Li = []
    Khan = []
    #candidate_names = set() # A complete list of candidates who received votes
    for row in csvreader: 
        voters.append(row[0])
        #candidate_names.add(row[2]) # A complete list of candidates who received votes
        if row[2] == "Correy":
            Correy.append(row[2])
        elif row [2] == "Li":
            Li.append(row[2])
        elif row[2] == "O'Tooley":
            Otooley.append(row[2])
        elif row[2] == "Khan":
            Khan.append(row[2])
# Printing Total Votes  
    print("Total Votes: " + str(len(voters)))
    print("-----------------------")
    #print (candidate_names) # A complete list of candidates who received votes
    

# The percentage of votes each candidate won
    Correy_percent = round((len(Correy)/len(voters)*100), 2)
    #print(Correy_percent)
    Li_percent = round((len(Li)/len(voters)*100), 2)
    #print(Li_percent)
    Otooley_percent = round((len(Otooley)/len(voters)*100), 2)
    #print(Otooley_percent)
    Khan_percent = round((len(Khan)/len(voters)*100), 2)
    #print(Khan_percent)
# The total number of votes each candidate won
    #print(str(len(Correy)))
    #print(str(len(Li)))
    #print(str(len(Otooley)))
    #print(str(len(Khan)))

# The winner of the election based on popular vote
    if Correy_percent > max(Li_percent, Otooley_percent, Khan_percent):
        Winner = "Correy"
    elif Li_percent > max(Correy_percent, Otooley_percent, Khan_percent):
        Winner = "Li"
    elif Otooley_percent > max(Correy_percent, Li_percent, Khan_percent):
        Winner = "O'Tooley"
    else:
        Winner = "Khan"
    #print(Winner)

# Printing everthing else 
    print(f"Correy: {Correy_percent}% ({(str(len(Correy)))})")
    print(f"Li: {Li_percent}% ({(str(len(Li)))})")
    print(f"O'Tooley: {Otooley_percent}% ({(str(len(Otooley)))})")
    print(f"Khan: {Khan_percent}% ({(str(len(Khan)))})")
    print("-----------------------")
    print(Winner)
    print("-----------------------")