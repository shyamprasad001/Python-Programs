word = input()
length = len(word)
first_letter = word[0]
second_letter = word[length - 1]
result = (first_letter != second_letter)
print(result)