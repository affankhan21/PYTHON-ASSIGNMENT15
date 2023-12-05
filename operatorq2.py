class Distance:
    def __init__(self,km,m,cm):
        self.km=km
        self.m=m
        self.cm=cm
    def __del__(self):
        print("object destroyed ")    
    def __add__(self,other):
        return self.km+other.km,self.m+other.m,self.cm+other.cm   
    def __sub__(self,other):
        return self.km-other.km,self.m-other.m,self.cm-other.cm       
print("--------------------------------------")
d1=Distance(50,40,30)
d2=Distance(60,56,78)
print("======================================")
res=d1+d2
print("DISTANCE ADDITION IS ",res)
d4=Distance(56,78,45)
d5=Distance(56,34,12)
res1=d4+d5
print("DISTANCE ADDITION IS ",res1)
