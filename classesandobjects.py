class goa:
    name = ""
    happy = ""
    def drink(self):
        print("lets party")
    def dance(self):
        print("lets dance")

steve = goa()
tony = goa()

tony.name = "tony"
steve.name = "steve"
steve.drink = "no"
tony.drink = "yes"
print(steve.name)
print("drink",steve.drink)
print(tony.name )
print("drink",tony.drink)
