import nltk
from nltk import *

# Import the data we gathered using sephora.py in read-only mode
comment_file = open("comment.txt", "r", encoding='utf-8')
data_text = comment_file.read()
comment_file.close()

# Tokenize the dataset 
tokens = nltk.word_tokenize(data_text)

# Create a frequency distribution 
fdist = FreqDist(tokens)
print(fdist.most_common(50))	
