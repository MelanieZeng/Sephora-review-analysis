import nltk  
from nltk.text import Text  
from nltk import *

# Import the data we gathered using sephora.py in read-only mode
commentfile = open("comment.txt", "r", encoding="utf-8")
comment_r = commentfile.read()
commentfile.close()

# Tokenize the dataset and get rid of words less than 3 characters (or said from a more literal code perspective, only keep words longer than 3 characters)
tokens = nltk.word_tokenize(comment_r)
tokens = [w for w in tokens if len(w) > 3]

# Create a frequency distribution to find the 150 most common words in the dataset
comment_freq = FreqDist(tokens)
print(comment_freq.most_common(150))

# Find all the long words (words longer than 15 characters) as we believe these to be of significance 
long_words = [w for w in set(tokens) if len(w) > 15]
print(long_words)

# Search the dataset for keywords that we've deemed to be keywords 
comment_text = Text(tokens)
comment_text.concordance("told")
comment_text.concordance("refund")
comment_text.concordance("shipping")
comment_text.concordance("samples")
comment_text.concordance("gift")
comment_text.concordance("package")
comment_text.concordance("gift-with-purchase")
