class String:
    def __init__(self, value):
        self.value = value

    def __iadd__(self, other):
        self.value += other.value
        return self

    def toLower(self):
        return self.value.lower()

    def toUpper(self):
        return self.value.upper()

s1 = String("Hello")
s2 = String("World")
s1 += s2
print("Concat:", s1.value)
print("Lower:", s1.toLower())
print("Upper:", s1.toUpper())