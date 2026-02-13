first_word = input()
second_word = input()
start_index = int(input())
second_word_length = len(second_word)
end_index = start_index + second_word_length
part = first_word[start_index:end_index]
print(part == second_word)