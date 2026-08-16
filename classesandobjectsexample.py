class student():
    def __init__(self):
        self.name = ""
        self.rollnu = 0
        
    def display(self):
        print("name:",self.name)
        print("roll number:",self.rollnu)
        
flute = student()
flute.name = "krish"
flute.rollnu = 21

flower = student()
flower.name = "radha"
flower.rollnu = 22

flute.display()
flower.display()



    