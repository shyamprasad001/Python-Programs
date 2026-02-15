word_1 = input()
word_2 = input()
length_word_1 = len(word_1)
length_word_2 = len(word_2)
word_1_last_3_digits = word_1[(length_word_1 - 3):]
word_2_last_3_digits = word_2[(length_word_2 - 3):]
result = (word_1_last_3_digits == word_2_last_3_digits)
print(result)