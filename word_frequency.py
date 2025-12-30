#Text data for word frequency analysis

text = "python is easy and python is powerful"

print("\n" + "=" * 40)
print("WORD FREQUENCY ANALYSIS REPORT")
print("=" * 40)

print("\nOriginal Text")
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
for word, count in word_count.items():
    print(f"{word:10} : {count}")

#Find Most frequent Word

most_frequent_word = ""
highest_count = 0

for word, count in word_count.items():
    if count > highest_count:
        highest_count = count
        most_frequent_word = word

print("\nMost Frequent Word :")
print(f"{most_frequent_word} → {highest_count}")