# Add our dependencies.
import csv
import os
# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

total_votes = 0 
canidate_options = []
canidate_votes = {}
winning_candidate = 0
winning_count = 0
winning_percentage = 0
# Open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    # Read and print the header row.
    headers = next(file_reader)
    print("--------------------------------------\n")
    #Add to the total count
    for row in file_reader:
        total_votes += 1

        #Get Candidate names
        candidate_names = row[2]

        #If the candidate does not match any existing candidate.        
        if candidate_names not in canidate_options:
            canidate_options.append(candidate_names)
            
            #Declare dictionay key. Canidate names
            canidate_votes[candidate_names] = 0

        canidate_votes[candidate_names] +=1
        
    for candidate_name in canidate_votes:
        #print(candidate_name)
        votes = canidate_votes[candidate_name]
        vote_percentage = float(votes)/float(total_votes) *100
        #print(f"{candidate_name}: received {vote_percentage}% of the vote.")
        
        if (votes > winning_count) and (vote_percentage > winning_percentage) :
            #True
            winning_count = votes
            winning_percentage = vote_percentage

            #Set the winning_candidate equal to the candidate's name.
            winning_candidate = candidate_name
            

        print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
print("--------------------------------------\n")

print(f"\n{winning_candidate} is the winner \n")
print(f"With a total of {votes} votes \n")
print(f"Collecting around{winning_percentage:.1f}% of the vote \n")
print("--------------------------------------\n")