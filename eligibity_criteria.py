maths = int(input())
physics = int(input())
chemistry = int(input())
total = maths + physics + chemistry
print((maths >= 70 and physics >= 60 and chemistry >= 60) or (total >= 180))