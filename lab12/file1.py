class ComplexNumber:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def display(self):
        print(f"{self.real} + {self.imag}i")

    def add(self, other):
        return ComplexNumber(self.real + other.real, self.imag + other.imag)

    def subtract(self, other):
        return ComplexNumber(self.real - other.real, self.imag - other.imag)

    def multiply(self, other):
        real = self.real * other.real - self.imag * other.imag
        imag = self.real * other.imag + self.imag * other.real
        return ComplexNumber(real, imag)

    def divide(self, other):
        try:
            denominator = other.real ** 2 + other.imag ** 2
            real = (self.real * other.real + self.imag * other.imag) / denominator
            imag = (self.imag * other.real - self.real * other.imag) / denominator
            return ComplexNumber(real, imag)
        except ZeroDivisionError:
            print("Error: Cannot divide by zero complex number.")
            return None



c1 = ComplexNumber(4, 5)
c2 = ComplexNumber(2, 3)

print("First complex number:")
c1.display()
print("Second complex number:")
c2.display()

print("\nAddition:")
c1.add(c2).display()

print("Subtraction:")
c1.subtract(c2).display()

print("Multiplication:")
c1.multiply(c2).display()

print("Division:")
result = c1.divide(c2)
if result:
    result.display()