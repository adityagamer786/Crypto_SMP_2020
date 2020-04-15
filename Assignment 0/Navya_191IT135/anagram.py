s1 = input("Enter string1: ")
print(s1)
arr = [ 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101]
s2 = input("Enter string2: ")
print(s2)
p1 = 1
for i in s1:
    x = ord(i)-97;
    p1*=arr[x]
print(str(p1))
p2 = 1
for i in s2:
    x = ord(i)-97;
    p2*=arr[x]
print(str(p2))
if p1==p2:
    print("It is an anagram.")
else:
    print("It is not an anagram")