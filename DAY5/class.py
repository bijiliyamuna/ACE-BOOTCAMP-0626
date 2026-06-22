class Student:
    fee_hike=1.02
    def __init__(self,name,branch,rno,fee,yoj):
        self.sname=name
        self.sbranch=branch
        self.srno=rno
    @classmethod
    def hike(cls):
        return "I am a class method"
    @staticmethod
    def result(fname,lname):
        return f"{fname+lname}"


    def name(self):
        print(self.name)
        
    def __repr__(self):
        return f"{self.sname},{self.sbranch},{self.srno}"
    def __str__(self):
        return f"{self.sname},{self.sbranch},{self.srno}"
        
#s1=Student("abc","cse",123,1,2024)
#s2=Student("abc","cse",123,1,2024)
#print(s1.hike())
s1=Student.result("My","Friend")
print(s1)

#print(s1)
#print(s2)

#str="hello"
#print(str)
#print("1"+"2")
#print(str.__add__("1","2"))
