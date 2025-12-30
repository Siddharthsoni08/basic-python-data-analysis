#Text data for word frequency analysis

text = "python is easy and python is powerful"

print("Original Text")
print(text)

#Split Text into Words

words = text.split()

print("\nWord List: ")
print(words)

#Count word frequency 

word_count = {}

for word in words:
    if word in word_count:
        word_count[word] = word_count[word] + 1
    else:
        word_count[word] = 1

print("\nWord Frequency: ")
print(word_count)

#Find Most frequent Word

most_frequent_word = ""
highest_count = 0

for word, count in word_count.items():
    if count > highest_count:
        highest_count = count
        most_frequent_word = word

print("\nMost Frequent Wors :")
print(most_frequent_word, "→", highest_count)