""" 
1. Написать калькулятор математических выражений на базе шаблона проектирования
Интерпретатор с возможностью вывода последовательности вычислений, все исключительные
ситуации отловить try/except блоками, чтобы не дать программе упасть. Поддерживаемые
операции: умножение, деление, сложениек, разность, степень. На ввод программе можно 
передавать выражения типа:

python calc.py
? 10 * 2 + 3 ** 2
= 10 * 2 + 9
= 20 + 9
= 29

? 2.34 ** 2 - 6 / 0
= 5.4756 - 6 / 0
= Нельзя делить на 0
"""
from sys import stdin


class AbstractExpression(object):
    def interpret(self):
        pass


class Number(AbstractExpression):
    def __init__(self, number: str) -> None:
        self.number = float(number) if '.' in number else int(number)
    
    
    def interpret(self) -> int | float:
        return self.number


class PowerExpression(AbstractExpression):
    def __init__(self, left: Number, right: Number) -> None:
        self.left = left
        self.right = right
    
    
    def interpret(self) -> int | float:
        return self.left.interpret() ** self.right.interpret()
        


class MultiplicationExpression(AbstractExpression):
    def __init__(self, left: Number, right: Number) -> None:
        self.left = left
        self.right = right
    
    
    def interpret(self) -> int | float:
        return self.left.interpret() * self.right.interpret()


class DivisionExpression(AbstractExpression):
    def __init__(self, left: Number, right: Number) -> None:
        self.left = left
        self.right = right
    
    
    def interpret(self) -> int | float:
        return self.left.interpret() / self.right.interpret()


class AdditionExpression(AbstractExpression):
    def __init__(self, left: Number, right: Number) -> None:
        self.left = left
        self.right = right
    
    
    def interpret(self) -> int | float:
        return self.left.interpret() + self.right.interpret()


class SubtractionExpression(AbstractExpression):
    def __init__(self, left: Number, right: Number) -> None:
        self.left = left
        self.right = right
    
    
    def interpret(self) -> int | float:
        return self.left.interpret() - self.right.interpret()


class Parser(object):
    def analyze(self, line):
        line = line.strip()
        
        if line == 'exit':
           return True
        
        elements = line.split()
        elements = Parser.check_elements(elements)
        sequence_of_operations = ['**', '*', '/', '+', '-']
        for operator in sequence_of_operations:
            operator_count = elements.count(operator)
            for i in range(operator_count):
                index_of_operator = elements.index(operator)
                left, right = Number(elements[index_of_operator - 1]), Number(elements[index_of_operator + 1])
                result = Parser.make_operation(left, operator, right)
                print(result)
        
        return False
    
    
    @staticmethod
    def check_elements(elements: list) -> list:
        """
        Check first element and length elements for valid
        
        :param elements: list of element
        :returns: return list of element
        """
        if elements[0] == '?':
            elements.pop(0)
        else:
            raise IndexError
        
        if len(elements) < 3:
            raise IndexError
        
        return elements
    
    
    @staticmethod
    def make_operation(left: Number, operator: str, right: Number) -> int | float:
        result = 0
        if operator == '**':
            result = PowerExpression(left, right).interpret()
        elif operator == '*':
            result = MultiplicationExpression(left, right).interpret()
        elif operator == '/':
            result = DivisionExpression(left, right).interpret()
        elif operator == '+':
            result = AdditionExpression(left, right).interpret()
        elif operator == '-':
            result = SubtractionExpression(left, right).interpret()
        else:
            raise IndexError
        
        return result
        

for line in stdin:
    parser = Parser().analyze(line)
    
    if parser:
        break