a = int(input("Enter your age: "))
print("your age is:",a)

if(a>18):
    print("you can drive")
else:
    print("you cannot drive")




        
num = int(input("enter the value :\n"))
if(num<0):
    print("number is negative")
elif(num == 0):
    print("number is zero")
else:
    print("number is positive")
  

# nested loop
num=int(input("enter the number"))
if(num < 0):
    print("Number is negative.")
elif(num >0):
    if(num <= 10):
        print("Number is between 1-10")
    elif(num > 10 and num <= 20):
        print("number is between 11-20")
    else:
        print("Number is greater than 20")
else:
    print("Number is zero")

  