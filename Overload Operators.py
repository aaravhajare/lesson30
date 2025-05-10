class A():

    def __init__(self,a):
        self.a = a

    def __lt__(self,other):
        if  (self.a < other.a):
            return "ob1 is less than ob2n "
        else :
            return False

    def __eq__(self,other):
        if (self.a == other.a):
            return "ob1 is equal to ob2"
        else:
            return False
        
ob1 = A(10)
ob2 = A(20)
print(ob1 < ob2)

print(ob1 == ob2)

