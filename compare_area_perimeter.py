length = int(input())
breadth = int(input())

Area = length * breadth
Perimeter = 2 * (length + breadth)

result = (Area <= Perimeter)
print(result)