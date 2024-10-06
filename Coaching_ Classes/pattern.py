
def prime_num(num):
    if num>1:
        for i in range(2,num):
            if num%i==0:
                print('It is not prime number')
                break
        else:
            print(num," is prime number")
    else:
        print(num,'it not prime number')
num=int(input("Enter the number"))
result=prime_num(num)

print(result)