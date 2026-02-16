s1 = input()
s2 = input()
s2_length = len(s2)
first_part_s1 = s1[:s2_length]
result = (first_part_s1 == s2)
print(result)