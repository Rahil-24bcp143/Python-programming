class Time:
    def __init__(self, h, m, s):
        self.h = h
        self.m = m
        self.s = s

    def add(self, other):
        s = self.s + other.s
        m = self.m + other.m + s // 60
        h = self.h + other.h + m // 60
        return Time(h % 24, m % 60, s % 60)

    def display(self):
        print(f"{self.h:02}:{self.m:02}:{self.s:02}")

t1 = Time(10, 45, 30)
t2 = Time(2, 30, 40)
t3 = t1.add(t2)
t3.display()