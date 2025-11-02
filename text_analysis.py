# Text Analysis Example
from collections import Counter
import string

# Sample text
text = """
Artificial Intelligence (AI) is transforming industries across the world.
It enables automation, enhances decision-making, and drives innovation.
Python is one of the most popular languages for AI development.
"""

text = text.strip()

# python
def count_letter_frequencies(text):
    letters = [c for c in text.lower() if c.isalpha()]
    counts = Counter(letters)
    total_letters = len(letters)

    print("\n🔤 Letter Frequency:")
    print(f"Total Letters: {total_letters}")
    for letter in sorted(counts):
        print(f"{letter}: {counts[letter]}")

# 1. Clean and preprocess text
def clean_text(text):
    text = text.lower()  # convert to lowercase
    text = text.translate(str.maketrans("", "", string.punctuation))  # remove punctuation
    return text

cleaned_text = clean_text(text)

# 2. Tokenize (split into words)
words = cleaned_text.split()

# 3. Word frequency count
word_count = Counter(words)

# 4. Basic statistics
num_words = len(words)
num_unique_words = len(set(words))
num_sentences = text.count('.')  # simple sentence count
num_characters = len(text)

# 5. Display results
print("📊 Text Analysis Summary:")
print(f"Total Characters: {num_characters}")
print(f"Total Words: {num_words}")
print(f"Unique Words: {num_unique_words}")
print(f"Total Sentences: {num_sentences}")
print("\n🗣️ Top 5 Most Common Words:")
for word, freq in word_count.most_common(5):
    print(f"{word}: {freq}")

print(f"\n🔤 Letter Frequency Analysis:")
count_letter_frequencies(text)
exit(0)