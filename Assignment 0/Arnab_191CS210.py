import math

#Angrams Checking
def is_anagram(s1, s2):
    ht = dict()

    if len(s1) != len(s2):
        return False

    for i in s1:
        if i in ht:
            ht[i] += 1
        else:
            ht[i] = 1
    for i in s2:
        if i in ht:
            ht[i] -= 1
        else:
            ht[i] = 1
    for i in ht:
        if ht[i] != 0:
            return False
    return True
#To check Prime number
primes=[]
def is_prime(x):
    global primes
    for divisor in primes:
        if divisor>math.sqrt(x):
            break
        if x%divisor==0:
            return False
    primes.append(x)
    return True
#Prime factorization
def factorize(x):
    primefactors=[]
    divisor=2
    while x > 1:
        if(is_prime(divisor)):
            if x % divisor==0:
                x=x/divisor
                primefactors.append(divisor)
            else:
                divisor+=1
        else:
            divisor+=1
    return primefactors
#Total number of factors
def factors(m):
    p=1
    s=1
    params=factorize(m)
    params.append(0)
    l=len(params)
    l-=1
    for i in range(l):
        if params[i]==params[i+1]:
            p+=1
        else:
            p+=1
            s*=p
            p=1
    print("Number of factors:", s)
#Main Program
print("1.First Program(Anagram)\n"
      "2.Second Program(Factors)\n"
      "Enter the choice:")
ch=(int)(input())
if(ch==1):
    #Enter the text from user
    print("Enter two texts:")
    s1 = input()
    s2 = input()
    #Changing to lower cases
    s1 = s1.replace(" ", "").lower()
    s2 = s2.replace(" ", "").lower()
    #Checking anagram
    bool=is_anagram(s1,s2)
    if(bool==True):
        print("Anagrams")
    else:
        print("Not Anagrams")
elif(ch==2):
    #Factors
    print("Enter a Number:")
    number = int(input())
    factors(number)
else:
    print("Wrong input")