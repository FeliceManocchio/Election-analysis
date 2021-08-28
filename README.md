# Election-analysis
Election Result Analysis in Python

## Overview and Purpose
In this Module we set out to analyze the election results saved in a .csv file containing all of the votes cast in 3 counties in Colorado(Jefferson, Denver, and Arapahoe). The file hold a unique ballot ID(voter) what county they are from, and who they voted for. Our mission was to develop a program that runs through the large .csv file and takes the count of each ballot and count them up in respect to county and candidate. In our analysis we will break down the quantity of votes down to the county level for each candidate and the percentage of the total votes in the respective county for each running candidate. The data collected will then presented in an easy to read text file presenting our findings for simple declaration of the winner and their margin of victory. 
## Election Audit Results
### Breakdown of Voter Distribution

Attached below is a clear representation of the findings we discovered during our election audit. The image depictes the following

- There were 369,711 total votes cast in the election that took place

- Individual county breakdown of votes are as follows
  - Jefferson had 38,855 total votes which held 10.5% of the total votes cast in this analysis
  - Denver had 306,055 total votes which held 82.8% of the total votes cast in this analysis
  - Arapahoe had 24,801 total votes cast which held 6.7% of the total votes cast in this analysis

- Denver had the largest voter turnout leading with 82.8% of the total votes cast in the election

- The individual candidate breakdown of votes are as follows
  - Charles Casper Stockham with 85,213 total votes which held 23% of the total votes cast
  - Diana DaGette with 272,892 total votes which held 73.8% of the total votes cast
  - Raymon Anthony Doane with 11,606 total votes which held 3.1% of the total votes cast

- The clear winner of the election is therefore Diana Degette with 272,892 votes commanding 73.8% of the total votes in the election
![Election_results](/Election_Images/Election_results.png)
## Election Audit Summary
### Modification for Future Usage

The analysis ran in this module is very straight forward in analyzing voter data in a very large .csv file. The way our code is currently written as long as there is a candidate name in the "C" column and a county in the "B" column of our file we can accurately portray the above information for any candidate across various counties in any election. If we wanted to take a deeper dive into the analytics of the results or increase the scale of the analysis like say dd it on a national level we wold adjust a handful of variables in the code and it would be consistant throughout. If we wanted to expand on the national level we would just add a level of analysis finding the count and percentage of votes at the state level. To do so this we would add an additional variable referencing the state tallies then within that if statement break it down by county if we found the county talley relevant to our total analysis. In step 4a where we set our county variables we could instead set state variables for properly segregating regional tallies of the candidate voted for. 
