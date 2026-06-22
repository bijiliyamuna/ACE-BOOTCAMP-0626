class Student:
    def __init__(self,name,branch,rno):
        self.sname=name
        self.sbranch=branch
        self.srno=rno
    @property
    def from_branch(self):
        return self.sbranch
    @from_branch.setter
    def from_branch(self,branch):
        self.sbranch=branch
    @from_branch.deleter
    def from_branch(self):
        self.sbranch=None
s=Student("yamuna","cse",123)
print(s.sbranch)
s.from_branch="csm"
print(s.sbranch)
del from_branch
print(s.sbranch)
