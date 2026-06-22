from abc import ABC,abstractmethod
class AbstractDemo:
    @abstractmethod
    def absd(self):
        pass
    def bcte(self):
        return "I am method with body"
class Main(AbstractDemo):
    def bcte(self):
        return "I am method with body"
m=Main()
print(m.absd())
print(m.bcte())
