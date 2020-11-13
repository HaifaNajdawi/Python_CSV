import os
import csv

#set path for the file 
csv_path= os.path.join('resources','election_data.csv')

# open the Csv  
with open (csv_path) as file_path:
    csv_reader=csv.reader(file_path,delimiter=",")
    #run over the header
    next(csv_reader)

    rows = list(csv_reader) 
    #length for the rows
    votes = len(rows)

    print(votes)

    # create dictionary
    candidate_dict = {}
    candidate_percentage=""

    # loop through the rows looking for keys and values
    for row in rows:

        if row[2]  in candidate_dict:
            candidate_dict[row[2]] += 1
        else: 
            candidate_dict[row[2]] = 1
    #loop through the dictionary to get values 
    for candidate in candidate_dict:

        candidate_percentage += f"{candidate}: {candidate_dict[candidate] / votes:.3%} ({candidate_dict[candidate]})\n"
    #find the key has the maximum value
    max_key = max(candidate_dict, key=candidate_dict.get)

# Set variable for output file 
output_path = os.path.join('analysis','output.txt')

# open the output file 
with open (output_path,'w',newline="") as text_file:

    #write the result to text file 
    text_file.write("Election Results\n")
    text_file.write("---------------------\n")
    text_file.write(f"Total Votes: {votes}\n")
    text_file.write("---------------------\n")
    text_file.write(f"{candidate_percentage}" )
    text_file.write("---------------------\n")
    text_file.write(f"Winner: {max_key}\n")
    text_file.write("---------------------\n")

    
    


