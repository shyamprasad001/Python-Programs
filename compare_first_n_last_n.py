word = input()
N = int(input())
word_length = len(word)
first_N_digits_word = word[:N]
last_N_digits_word = word[(word_length - N):]
result = (first_N_digits_word != last_N_digits_word)
print(result)