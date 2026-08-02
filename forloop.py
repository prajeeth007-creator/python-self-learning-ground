#for i in range(1, 11):
   # print(i,"x5=",i*5
#program ends here ---------------------------------------------------------------------------
    
#count = 0
#for i in range(1,11):
    #if(i%2 == 0):
       # print(i)
   # count = count + 1

#print("total even numbers:", count)

#program ends here ---------------------------------------------------------------------------

e_count = 0
o_count = 0
for i in range(1,11):
    if(i%2 == 0):
        print(i,"even number")
        e_count = e_count + 1
    else:
        print(i,"odd number")
        o_count = o_count + 1

print("total even numbers:", e_count)
print("total odd numbers:", o_count)
