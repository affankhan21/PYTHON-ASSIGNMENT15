class complex_number:
    def __init__(self,real,imag=0):
        self.real=real
        self.imag=imag
    def __del__(self):
        print("COMPLEX NUMBER OBJECT DELETED ")
    # overloading + operator
    def __add__(self,other):
        return self.real+other.real,self.imag+other.imag
    # overloading - operator
    def __sub__(self,other):
        return self.real-other.real,self.imag-other.imag             
c1=complex_number(24,56)
c2=complex_number(5,65)
print("======================================")
result=c1+c2 
print("ADDITION IS ",result) 
print("======================================")
result11=c1-c2 
print("SUBTRACTION IS ",result11)  
print("======================================")           