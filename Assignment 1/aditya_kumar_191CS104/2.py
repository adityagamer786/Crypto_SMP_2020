x = input("Enter num: ")
x = int(x, 16)
y = "686974207468652062756c6c277320657965" 
y = int(y, 16)
xor = x^y
xor = hex(xor)
print(str(xor)[2:])