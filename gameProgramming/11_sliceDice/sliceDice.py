alphabet = 'abcdefghijklmnopqrstuvwxyz'
myString = 'Go and make me a sandwich'

print(alphabet[0])
print(alphabet[-1])

# Slicing
print(alphabet[0:4]) # Slice UP TO second index.
# alphabet[start:stop]

# Slice from the Start
print(alphabet[:7])

# Slice to the End
print(alphabet[12:])

# Slice the Whole Thing
print(alphabet[:])

# Negative Index Slicing
print(alphabet[-7:-2])

print(myString[3:10])
print(myString[:11])
print(myString[15:])
print(myString[:])
print(myString[-10:-3])