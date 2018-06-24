num1 = int(input("Enter a first number : "))

num2 = int(input("Enter the second number : "))

for num in range (num1, num2+1):
    if num > 1:
        for i in range (2, num):
            if (num%i == 0):
                #print (num, " is not a prime number")
                break
        else:
            print(num, " is a prime number")
#else:
 #   print()

    
'''
for i in range (1, 100):
    print ("The Prime numbers are : ")
    for j in range (1, i):
        if (i%j != 0):
            print (i)
'''
