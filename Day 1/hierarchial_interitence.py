
class A:
    def func1(self):
        print("class A")

class B(A):
    def func2(self):
        print("class B")

class C(B,A):
    def func3(self):
        print("class C")


obj = C()
obj.func1()

