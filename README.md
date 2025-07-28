# Quantifying-Legal-Complexity
## What is this
 The purpose of this project is to generate quantitative data about the complexity of law contained in a database of justian's digest (digest.db)
 ## How to reproduce data and graphs
 you can create a file containing the data (a dictionary containing all the information about each section) using:                  
python3 generate_dictionary.py digest.db > dictionary.txt
 
 and then you can produce graphs and figures from the data using:                                                      
 python3 graphs_and_tables.py dictionary.txt
