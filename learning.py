a = int(input("enter the number:"))
b = int(input("enter the number:"))

operation = input("add/sub/multiply/div:")

if (operation=="add"):
   print(a+b)
elif (operation=="sub"):
   print(a-b)
elif(operation=="multiply"):
   print(a*b)
elif(operation=="div"):
   print(a/b)
else:
    print("invalid operation")
