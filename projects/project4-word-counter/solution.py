sentence = input("Enter a sentence: ")
words = sentence.lower().split()

# total word count
total_words = len(words)

# character count (no spaces)
total_chars = len(sentence.replace(" ", ""))

# word frequency
frequency = {}
for word in words:
    if word in frequency:
        frequency[word] += 1
    else:
        frequency[word] = 1

# print results
print(f"Total words: {total_words}")
print(f"Total characters (no spaces): {total_chars}")
print("Word frequency:")
for word, count in frequency.items():
    print(f"{word}: {count}")
