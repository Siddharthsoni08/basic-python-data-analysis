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
