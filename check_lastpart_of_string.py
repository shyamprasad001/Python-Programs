A = input()
B = input()
A_length = len(A)
B_length = len(B)

start_index = A_length - B_length
part = A[start_index:]
result = (part == B)
print(result)