from random import randint

s1 = input("Enter string 1:")
s2 = input("Enter string 2:")

if len(s1) != len(s2):
    print('Not anagram')
    exit(0)

ag = []
bg = []
for i in range(5):
    ag.append(randint(1,25))
for i in range(5):
    bg.append(randint(0,25))

for a in ag:
    for b in bg:
        hash1 = 0
        for ch in s1:
            hash1 += (a*ord(ch) + b) % 29
        hash2 = 0
        for ch in s2:
            hash2 += (a*ord(ch) + b) % 29
        if hash1 != hash2:
            print("Not anagram")
            exit(0)

print("The probability that they are not anagram is same as that of a large UFO hitting the earth in next 1 second")
print("In other words, they are anagram")
