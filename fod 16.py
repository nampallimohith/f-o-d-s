import string
from collections import Counter
reviews = [
    "This product is great! I love it.",
    "The quality of this product is poor.",
]
translator = str.maketrans('', '', string.punctuation)
all_words = [word.lower().translate(translator) for review in reviews for word in review.split()]
word_freq = Counter(all_words)
sorted_word_freq = dict(sorted(word_freq.items(), key=lambda item: item[1], reverse=True))
print("Word Frequency Distribution:")
for word, freq in sorted_word_freq.items():
    print(f"{word}: {freq}")
