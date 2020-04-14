x=int(input("Enter the number\n"))
i=1
while i*i<=x:
        if x%i==0:
                print(i,end=" ")
                if x//i!=i:
                        print(x//i,end=" ")
        i=i+1
