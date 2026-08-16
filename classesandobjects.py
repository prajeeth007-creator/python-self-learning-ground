#class goa:
    #name = ""
    #happy = ""
   # def drink(self):
  #      print("lets party")
 #   def dance(self):
 #       print("lets dance")

#steve = goa()
#tony = goa()

#tony.name = "tony"
#steve.name = "steve"
#steve.drink = "no"
#tony.drink = "yes"
#print(steve.name)
#print("drink",steve.drink)
#print(tony.name )
#print("drink",tony.drink)

#program ends here_____________________________

class goa():
    def __init__ (self):
        self.lead = "steve"
        self.tech = "tony"
        self.tonydrink = "yes drink"
        self.stevedrink = "no drink"
        
name = goa()
print(name.lead)
print(name.stevedrink)
print(name.tech)
print(name.tonydrink)
        
        

