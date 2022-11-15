
import os
import csv

 
csvpath=os.path.join("..","/Users/katienguyen/Assignment 3/Resources/PyPoll","election_data.csv")
with open(csvpath,) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
    
   
    votes = []
    ctry = []
    candidates_list = []
    CharlesCasperStockham = []
    DianaDeGette = []
    RaymonAnthonyDoane = []
    CharlesCasperStockham_votes = 0
    DianaDeGette_votes = 0
    RaymonAnthonyDoane_votes = 0

    
    for row in csvreader:
        votes.append(int(row[0]))
        ctry.append(row[1])
        candidates_list.append(row[2])

    # Counting total of votes
    total_votes = (len(votes))
    
    # Spcify votes per candidate
    for candidate in candidates_list:
        if candidate == "Charles Casper Stockham":
            CharlesCasperStockham.append(candidates_list)
            CharlesCasperStockham_votes = len(CharlesCasperStockham)
            
        elif candidate == "Diana DeGette":
            DianaDeGette.append(candidates_list)
            DianaDeGette_votes = len(DianaDeGette)
            
        else:
            RaymonAnthonyDoane.append(candidates_list)
            RaymonAnthonyDoane_votes = len(RaymonAnthonyDoane)
   
    # Percentages
    CharlesCasperStockham_percent = round(((CharlesCasperStockham_votes / total_votes) * 100), 3)
    DianaDeGette_percent = round(((DianaDeGette_votes / total_votes) * 100), 3)
    RaymonAnthonyDoane_percent = round(((RaymonAnthonyDoane_votes / total_votes) * 100), 3)
    
    
    # Winner 
    if CharlesCasperStockham_percent > max(DianaDeGette_percent, RaymonAnthonyDoane_percent):
        winner = "CharlesCasperStockham"
    elif DianaDeGette_percent > max(CharlesCasperStockham_percent, RaymonAnthonyDoane_percent):
        winner = "DianaDeGette"  
    else:
        winner = "RaymonAnthonyDoane"


    # Final Statement
    print(f'''Election Results
------------------------------
Total Votes: {total_votes}
------------------------------

CharlesCasperStockham_percent: {CharlesCasperStockham_percent}% ({CharlesCasperStockham_votes})
----------------------------
DianaDeGette: {DianaDeGette_percent}% ({DianaDeGette_votes})
RaymonAnthonyDoane: {RaymonAnthonyDoane_percent}% ({RaymonAnthonyDoane_votes})
--------------------------------
Winner: {winner}
--------------------------------''')


    # The outputs
    file = open("output.txt","w")
    file.write(f'''Election Results
-------------------------------
Total Votes: {total_votes}
--------------------------------
CharlesCasperStockham_percent: {CharlesCasperStockham_percent}% ({CharlesCasperStockham_votes})
DianaDeGette: {DianaDeGette_percent}% ({DianaDeGette_votes})
RaymonAnthonyDoane: {RaymonAnthonyDoane_percent}% ({RaymonAnthonyDoane_votes})
-----------------------------
Winner: {winner}
-------------------------------''')

    file.close()
