class A:
    def func1(self):
        print("class A")

class B:
    def func2(self):
        print("class B")

class C(B,A):
    def func2(self):
        print("class C")


obj = C()
obj.func1()
obj.func2()

