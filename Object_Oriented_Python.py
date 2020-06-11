# refactor to change variable name
# ctrl+f= find something
# ctrl+/= to comment/ uncomment
# alt+shift+c= recent changes

class Computer:

    def __init__(self, cpu, ram):
        print("constructor")
        self.cpu = cpu
        self.ra = ram

    def config(self):
        val = "Config is " + str(self.cpu) + " and " + str(self.ra)
        print(val)

    def compare(self, other):
        if self.ra == other.ra:
            return True
        else:
            return False


class Student:
    school = "Ideal"  # class variable

    def __init__(self, m1, m2, m3):
        # instance variable
        print("constructor")
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3
        self.lap = self.Laptop()

    def get_m1(self):
        return self.m1

    def set_m1(self, value):
        self.m1 = value

    def avg(self):
        return (self.m1 + self.m2 + self.m3) / 3

    @classmethod
    def getschool(cls):
        return cls.school

    @staticmethod
    def getinfo():
        print("This is static method")

    # inner class
    class Laptop:
        def __init__(self):
            self.cpu = 'i5'
            self.ram = 8

    # operator overloading
    def __add__(self, other):
        m1 = self.m1 + other.m1
        m2 = self.m2 + other.m2
        m3 = self.m3 + other.m3
        return Student(m1, m2, m3)

    def __gt__(self, other):
        r1 = self.m1 + self.m2 + self.m3
        r2 = other.m1 + other.m2 + other.m3
        # return True if r1 > r2 else False
        return r1 > r2 and True or False

    def __str__(self):
        return '{} {} {}'.format(self.m1, self.m2, self.m3)

    # method overloading not in pythod. do it by trick
    def sum(self, a=None, b=None, c=None):
        s = 0
        if a is not None and b is not None and c is not None:
            s = a + b + c
        elif a is not None and b is not None:
            s = a + b
        else:
            s = a
        return s

# multiple inheritance can be possible here by Method Resolution Order (MRO) left to right
class ChildStudent(Student):

    def __init__(self, m1, m2, m3):
        print("child constructor")
        super().__init__(m1, m2, m3)

    @staticmethod
    def showchild():
        print("Child")


# Start Computer
com = Computer('i5', 20)
com1 = Computer(4, 20)
com.config()
com1.config()

if com.compare(com1):
    print("same")
else:
    print("different")
# End Computer

# Start Student
std = Student(12, 2, 4)
print(std.set_m1(45))
print(std.get_m1())
print(std.avg())
print(Student.getschool())
Student.getinfo()
lap = Student.Laptop()
print(lap.cpu)
print(std.lap.cpu, std.lap.ram)

# call operator overloading
s1 = Student(100, 2, 3)
s2 = Student(12, 16, 6)
s3 = s1 + s2
print('+ operating overloading=', s3.m1, s3.m2, s3.m3)
print("s1 greater") if s1 > s2 else print("s2 greater")
strvalue = s1 > s2 and "s1 greater" or "s2 greater"
print(strvalue)
print(str.__add__('a', 'b'))
print(2 + 2)
print(s1)

# method overloading
print("sum=",s1.sum(1,2))
# End Student

# Start ChildStudent
cs = ChildStudent(1, 2, 3)
print(cs.getschool())
print(cs.showchild())
# End ChildStudent
