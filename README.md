# Election Analysis using PyPoll

## Overview of Election Audit
This project revolves around helping Tom, a Colorado Board of Elections employee, with an election audit to determine the total number of votes, the candidates and the numbers of votes they each received, and determine the winning candidate. Automating this task in Python for this congressional election audit can help the board for senatorial election audits and even local election audits in the future. 

## Election Audit Results
Using the data provided for the congressional election in Colorado there were three candidates:
- Charles Casper Stockham
- Diana DeGette
- Raymon Anthony Doane
The overall winner is **Diana Degette**. As shown below she had the majority of the votes (73.8%)

![Overall Vote Outcome](https://github.com/ayaakoub/Election-Analysis/blob/main/Resources/Candidates_Votes.PNG)

There were a total of three counties:
- Jefferson 
- Denever 
- Arapahoe
The total voters from the three counties were 369,711 votes with <ins>Denver</ins> having the largest turnout (82.8% of voters). Below is a breakdown of the total number of voters by county.

![Overall County Outcome](https://github.com/ayaakoub/Election-Analysis/blob/main/Resources/County_Votes.PNG)

## Election Audit Summary 

The python PyPoll module is versatile and can be used by the election comission for any election audit. However a few things must be taken into account:
- The python module assume the county name is in the second column and the candidate is in the third column of the CSV file. If that is not the case then the for loops must be adjusted to reflect the change. The following two lines must be adjusted to have the number in the brackets = (the column number - 1). That's because the CSV column index starts at 0 rather than 1. 
  -         candidate_name = row[2]

            county_name = row[1]

- The other line to keep in mind is where the CSV file is kept as the path is extremly important in accessing the data. Currently the file should be in the same parent folder as the python file as the following code indicates. It should be within a folder called 'Resources' if the folder changes then the line must change accordingly. This also applies to the output file. If the election commission would like to change the output file folder the 'analysis' folder can be renamed to something else and will have to be reflected in the code accordingly.
  -         file_to_load = os.path.join("Resources", "election_results.csv")
  
            file_to_save = os.path.join("analysis", "election_analysis.txt")


