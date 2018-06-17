# Description 
This program crawls web text on a Sephora review page and returns the review ID, rating score, first name and location of the reviewer, their review text, and how many people found their review to be helpful. 
# Required Libraries 
Use the following pip commands in command prompt to install the necessary libraries. 
```
pip3 install requests 
pip3 install lxml
pip3 install beautifulsoup4
pip3 install nltk
```
# Todo List
Items are listed in order of importance. 
1. Save data in datafile properly (fix error of index out of range)
2. Low priority: filter out `<strong>` tag and `people` in array_helpful (may use replace())

# Solved Issues
1. Stop skipping over hidden paragraphs (when reviews are long and you have to click "see more", the crawler skips over these parts)
2. Fix 5, 4, 3, 2, 1 bug at the beginning of `rating` (for some odd reason the first 5 ratings on every page come in as 5, 4, 3, 2, 1 but that is incorrect)
