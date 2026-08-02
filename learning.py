#a = int(input("enter the number:"))
#b = int(input("enter the number:"))

#operation = input("add/sub/multiply/div:")

#if (operation=="add"):
  # print(a+b)
#elif (operation=="sub"):
 #  print(a-b)
#elif(operation=="multiply"):
 #  print(a*b)
#elif(operation=="div"):
#   print(a/b)
#else:
#    print("invalid operation")

#program ends here ---------------------------------------------------------------------------

#score = int(input("enter your score"))
#if score >= 70:
  #  print ("your eligible")
#else:
   # print("your not eligible")

#program ends here ---------------------------------------------------------------------------

salary = int(input("enter your salary:"))
age = int(input("enter your age:"))

if (salary > 25000 or age < 25):
    loan = int(input("enter your loan amount"))
    if(loan <= 50000):
        print("your eligible for loan")
    else:
        print("maximum amount is 50000")
    
else:
    print("your not eligible for loan:")
    
