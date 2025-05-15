class Calculator:
    def __init__(self, num1, num2):  # Corrected __init__
        self.num1 = num1
        self.num2 = num2

    def add(self):
        return self.num1 + self.num2

    def sub(self):
        return self.num1 - self.num2

    def mul(self):
        return self.num1 * self.num2

    def div(self):
        if self.num2 != 0:
            return self.num1 / self.num2
        else:
            return "Cannot divide by zero."

# Taking input
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

# Create object
cl = Calculator(num1, num2)

# Perform operations
ans1 = cl.add()
ans2 = cl.sub()
ans3 = cl.mul()
ans4 = cl.div()

# Print results
print("Addition:", ans1)
print("Subtraction:", ans2)
print("Multiplication:", ans3)
print("Division:", ans4)
