import os
import csv

election_data = os.path.join("Resources", "election_data.csv")

with open(election_data, 'r') as csvfile:
    csv_reader = csv.reader(csvfile)
    next(csv_reader)

    total_votes = 0
    candidates = {}

    for row in csv_reader:
        total_votes += 1

        candidate = row[2]

        if candidate in candidates:
            candidates[candidate] += 1
        else:
            candidates[candidate] = 1

election_results = 'Analysis/election_results.txt'

with open (election_results, 'w') as output:
    print("Election Results")
    print("")
    print("-------------------------")
    print("")
    print(f"Total Votes: {total_votes}")
    print("")
    print("-------------------------")
    print("")

    output.write("Election Results\n")
    output.write("\n")
    output.write("-------------------------\n")
    output.write("\n")
    output.write(f"Total Votes: {total_votes}\n")
    output.write("\n")
    output.write("-------------------------\n")
    output.write("\n")

    for candidate, votes in candidates.items():
        percentage = (votes / total_votes) * 100
        print(f"{candidate}: {percentage:.3f}% ({votes})")
        output.write(f"{candidate}: {percentage:.3f}% ({votes})\n")

    winner = max(candidates, key = candidates.get)

    print("")
    print("-------------------------")
    print("")
    print(f"Winner: {winner}")
    print("")
    print("-------------------------")
    print("")
    output.write("-------------------------\n")
    print("")
    output.write(f"Winner: {winner}\n")
    print("")
    output.write("-------------------------\n")