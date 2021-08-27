# Add our dependencies.
import csv
import os
# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

#Open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)
# Print each row in the CSV file.
    #for row in file_reader:
     #   print(row)
    # Read and print the header row.
    headers = next(file_reader)
    print(headers)
#Data to retrieve

##Total number of votes cast

##Complete list of candidates who received votes

##percentage of votes each candidate won

##tota number of votes each candidate won

##Winner of election based on popular vote

#Import the datetime class from the datetime module.
# Using the with statement open the file as a text file.

