import time
timestamp=time.strftime('%H:%M:%S')
print(timestamp)
hour=int(time.strftime('%H'))
print(hour)
minutes=int(time.strftime('%M'))
print(minutes)
seconds=int(time.strftime('%S'))
print(seconds)
# a=int(input("enter the time \n"))
if(6<=hour and 12>hour):
  print("Good morning sir")
elif(12<=hour and 16>hour):
  print("Good after noon sir")
elif(16<=hour and 19>hour):
    print("Good evening sir")
elif(19<=hour and 23>=hour):
    print("Good night sir")
else:
    print("Invalid time")