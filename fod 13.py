import string
from collections import Counter

with open('C:/Users/mohit/Documents/text.txt', 'r') as file:
    text = file.read()

translator = str.maketrans('', '', string.punctuation)
words = text.lower().translate(translator).split()
word_freq = Counter(words)
sorted_word_freq = dict(sorted(word_freq.items(), key=lambda item: item[1], reverse=True))
print("Word Frequency Distribution:")
for word, freq in sorted_word_freq.items():
    print(f"{word}: {freq}")
