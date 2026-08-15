#def avengers():
 #   return "assemble"
#a = avengers()
#print(a)
    
    
name = "top"
password = 2345

a = input("enter your name:")
b = int(input("enter your password:"))

def verification():
    if a == name and b == password :
        print("correct password and username")
    else:
        print("incorrect password or username")
        
verification()