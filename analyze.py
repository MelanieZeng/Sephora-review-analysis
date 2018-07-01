import nltk
import nltk.corpus  
from nltk.text import Text  
from nltk import *

commentfile = open("comment.txt", 'r', encoding="utf-8")

comment_r = commentfile.read()

commentfile.close()

tokens = nltk.word_tokenize(comment_r)

comment_freq = FreqDist(tokens)
print (comment_freq)

comment_freq = FreqDist(tokens)
comment_words = comment_freq.most_common(150)
print (comment_words)

set_words = set(tokens)
long_words = [w for w in set_words if len(w)>15]
print (long_words)

comment_text = Text(tokens)
comment_text.concordance('told')
comment_text.concordance('refund')
comment_text.concordance('shipping')
comment_text.concordance('samples')
comment_text.concordance('gift')
comment_text.concordance('package')
comment_text.concordance('gift-with-purchase')
