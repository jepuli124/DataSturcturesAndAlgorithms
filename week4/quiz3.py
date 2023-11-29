def hash(S):
    sum = 0
    for i in range(len(S)):
        sum += ord(S[i])
    return sum % 5


print(hash("dog"))
print(hash("cat"))
print(hash("bird"))
print(hash("worm"))
print(hash("fish"))
print(hash("cow"))
print(hash("wolf"))
print(hash("fox"))
print(hash("seal"))
print(hash("fly"))