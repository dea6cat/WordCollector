import collections
import pandas as pd
from collections import Counter 
import re
#Alexander Montolio #1072200  

#read file  "name"   and   "encoding"
file = open('bible.txt', encoding="utf8")
a= file.read()
# Stopwords
stopwords = set(line.strip() for line in open('stopwords.txt'))
stopwords = stopwords.union(set(['mr','mrs','one','two','said']))
# Instantiate dictionary, and for every word in the file, 
# Add to the dictionary if it doesn't exist. If it does, increase the count.
pages = {}
wordcount = {}
print("The books has the lenght "+str(len(a.split())))
# To eliminate duplicates, to split by punctuation, and use case demiliters.
for word in a.lower().split():
    word = word.replace(".","")
    word = word.replace(",","")
    word = word.replace(":","")
    word = word.replace("\"","")
    word = word.replace("!","")
    word = word.replace("â€œ","")
    word = word.replace("â€˜","")
    word = word.replace("*","")
    if word not in stopwords:
        if word not in wordcount:
            wordcount[word] = 1
        else:
            wordcount[word] += 1
# Print most common word
n_print = 10
print("\nOK. The {} most common words are as follows\n".format(n_print))
word_counter = collections.Counter(wordcount)
for word, count in word_counter.most_common(n_print):
    print(word, ": ", count)


#Most common letter
print("\nOK. The {} most common letters are as follows\n".format(n_print))
data = collections.Counter(''.join(a))
for data, count in data.most_common(n_print)[1:]:
    print(data, ": ", count)



#n: [] for n in names
matched = {}
m=0
xv=a.replace('"', '')
l1=[c for c in a]
l2=[ord(c) for c in l1]
n=len(a.split())
b = 300
v = n/b
z = round(v)
q=0

    
for i in range(0,z):
    q+=1
    #print(q)
    m+=1
    mm=str(m)
    n=sum(l2[q:300+q])
    matched.update({'page '+mm:n})
    

#print(matched)
max_key = max(matched, key=matched.get)
print("the page with gratest ASCII value is: "+max_key)
l2.sort()
first = chr(max(l2))
print("the character with gratest ASCII value is: " +first )


# sorting the list  
# printing the second last element 
#print("Second largest element is:", l2[-2]) 
#25743
#8212
# Close the file
file.close()
