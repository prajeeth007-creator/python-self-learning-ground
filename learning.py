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

    
tamil = int(input("enter your tamil mark:"))
english = int(input("enter your english mark:"))
maths = int(input("enter your maths mark:"))
science = int(input("enter your science mark:"))
social = int(input("enter your social mark:"))

f = (tamil + english + maths + science + social)/5
if f>= 35:
   print("your pass")
else:
   print("your fail")