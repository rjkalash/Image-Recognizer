

maxi=0
def gcd(x,y):
    if (x==0|y==0):
        print("Either of the number is zero")
    elif x==y:
        maxi=x
        return maxi
        

    else:
        for i in range(1, min(x,y)+1):
            if ((x%i)==0&(y%i)==0):
                maxi=i
    return maxi
            
                
a=int(input("Enter the number1:"))
b=int(input("Enter the number2:"))
print("The Gcd of given number is ",gcd(a,b))
