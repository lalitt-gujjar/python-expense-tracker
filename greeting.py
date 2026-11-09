a=int(input("enter the time \n"))
if(6<=a and 12>a):
  print("Good morning sir")
elif(12<=a and 16>a):
  print("Good after noon sir")
elif(16<=a and 19>a):
    print("Good evening sir")
elif(19<=a and 23>=a):
    print("Good night sir")
else:
    print("Invalid time")