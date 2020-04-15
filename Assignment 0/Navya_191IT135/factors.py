x = input("Enter a number: ")
y = int(x)
k = y
for i in range(1,int(y/2)+1):
    if k%i == 0:
        print(""+str(i))
print(str(k))       