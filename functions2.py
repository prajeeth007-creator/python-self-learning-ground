#def painter(msg):
    #print("i am",msg)
    
#painter("spiderman")


#def oddeven(b):
 #   if(b%2 == 0):
  #      print("this number is even")
  #  else:
 #       print("this number is odd")
        
#a = int(input("enter a:"))
#oddeven(a)
#program ends here ------------------------------------
def passfail(b):
    if(100 >= b >= 35):
        print("pass")
    elif(b<35):
        print("fail")
    else:
        print("not defined")
a = int(input("enter the mark:"))
passfail(a)

#program ends here --------------------------------------------

def count(x1,x2):
    for i in range(x1,x2):
        print(i)
a = int(input("enter the input:"))
b = int(input("enter the input:"))
count(a,b)
        