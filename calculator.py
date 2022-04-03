class calculator:

    #Constructor
    def __init__(self,input1,input2):
        self.input1 = input1
        self.input2 = input2 

    #Addition function
    def adder(self):
        return self.input1 + self.input2

    #Subtraction function
    def subtractor(self):
        return self.input1 - self.input2

    #Multiplication function
    def multiplier(self):
        return self.input1 * self.input2
    
    #Division function
    def divider(self):
        return self.input1 / self.input2

    #Clear function
    def clear(self):
        self.input1 = self.input2 = 0.0
        

    




input1 = float(input("Enter the first number: "))
input2 = float(input("Enter the second number: "))

newcalculator = calculator(input1,input2)

print("Addition of the two numbers: " , newcalculator.adder())
print("Subtraction of the two numbers: ", newcalculator.subtractor())
print("Multiplication of the two numbers: ", newcalculator.multiplier())
print("Division of the two numbers: ", newcalculator.divider())
print("After Clearing : ")
newcalculator.clear()
print("Input 1 = ",newcalculator.input1)
print("Input 2 = ",newcalculator.input2)


