import operator
import sys

# Read in file

sys.argv

file = open(sys.argv[1], "r") #Abre o segundo arquivo digitado no prompt

text = file.read()
textsize = len(text.split())
file.close()
# Count the words

words = {}

for word in text.split():
    if word.lower() in words:
        words[word.lower()] += 1 #Se a palavra já existem soma + 1
    else:
        words[word.lower()] = 1 

sortedwords = sorted(words.items(), key=operator.itemgetter(1), reverse=True)
sortedsize = len(sortedwords)

# Write the counted words into a new file

file = open(sys.argv[1][:-4] + "-count" + sys.argv[1][-4:], "w")

file.write(f"Total Words - {textsize}\nUnique Words - {sortedsize}\n\n")
for wordinfo in sortedwords:
    file.write(f"{wordinfo[0]} - {wordinfo[1]}\n")

file.close()

print("All counted!")