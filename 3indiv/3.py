text = input("Input text: ")
words = text.split(" ")

def checklength(word):
    if len(word) == 3:
        return True
    else:
        return False

counter = 0
for word in words:
    if checklength(word): counter += 1

print("Number of 3 length words: ", counter)