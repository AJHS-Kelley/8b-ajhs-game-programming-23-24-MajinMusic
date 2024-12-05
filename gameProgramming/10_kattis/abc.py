# input the integers
# .split() the 3 integers into separate variables.
# cast the 3 variables to integers (Changing one datatype to another).
# assign correct values from least to greatest
# A < B < C

integers = input()
a, b, c = integers.split()
a = int(a)
b = int(b)
c = int(c)

print(f"a: {a} b: {b} c: {c}")
while True:
    if b >= c:
        b, c = c, b
    if a >= b:
        a, b = b, a
    if a <= b <= c:
        break
print(f"a: {a} b: {b} c: {c}")

# input the string variable
# determine order of A, B, and C
# create correct string
# output string

order = input()
myString = ""

for i in range(len(order)):
    if order[i] == "A":
        myString += str(a) + " "
    elif order[i] == "B":
        myString += str(b) + " "
    else:
        myString += str(c) + " "

print(myString)

