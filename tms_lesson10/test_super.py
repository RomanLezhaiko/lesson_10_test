class A(object):
    def __init__(self) -> None:
        pass
    
    def interpret(self, op):
        print(op)


class B(A):
    def __init__(self) -> None:
        super().__init__()
    
    
    def interpret(self):
        super().interpret(1)


b = B()
b.interpret()