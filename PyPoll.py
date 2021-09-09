# The data we need to retrieve.
# 1. The total number of votes cast
# 2. A complete list of candidates who received votes
# 3. The poercentage of votes each candidate won
# 4. The total number of votees each candidate won
# 5. The winner of the election based on popular vote
import csv
import os
# assign a variable to load a file from a path
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path
file_to_save = os.path.join("analysis", "election_analysis.txt")
# open election results and read the file
with open(file_to_load) as election_data: 
    # To do: perform analysis
    # Read the file object with the reader function
    file_reader = csv.reader(election_data)
    # print the header row
    headers = next(file_reader)
    print(headers)
    # Print each row in the CSV file
    for row in file_reader:
        print(row)
    # Print the file object
    print(election_data)
# create afilename variable to a direct or indirect path to the file
file_to_save = os.path.join("analysis", "election_analysis.txt")
# Using the open() function with the "w" mode we will worite data to the file
open(file_to_save, "w")

# Using the with statement open the file as a text file
with open(file_to_save, "w") as txt_file:
    # Write some data to the file
    txt_file.write("Counties in the Election\n-\nArapahoe\nDenver\nJefferson")
# Close the file
election_data.close()


# Write three counties to the file
