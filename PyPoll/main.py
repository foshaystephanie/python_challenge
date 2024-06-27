import os
import csv

election_data = os.path.join("Resources", "election_data.csv")

with open(election_data, 'r') as csvfile:
    csv_reader = csv.reader(csvfile)
    next(csv_reader)

    total_votes = 0
    votes = {}