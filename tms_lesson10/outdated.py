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
from abc import abstractmethod


class AbstractExpression(object):
    """ 
    All Terminal and Non-Terminal expressions will implement an interpret method
    """
    @abstractmethod
    def interpret(self):
        pass


class Number(AbstractExpression):
    """ 
    Terminal Expression
    """
    def __init__(self, number: str) -> None:
        """ 
        :param number: number is float or int
        """
        self.number = float(number) if '.' in number else int(number)
    
    
    def interpret(self) -> int | float:
        """ 
        :returns: return number (int or float)
        """
        return self.number


class PowerExpression(AbstractExpression):
    """ 
    Non-Terminal Expression
    """
    def __init__(self, left: Number, right: Number) -> None:
        """ 
        :param left: left part of expression
        :param right: right part of expression
        """
        self.left = left
        self.right = right
    
    
    def interpret(self) -> int | float:
        """ 
        :returns: return power of left and right part
        """
        return self.left.interpret() ** self.right.interpret()


class MultiplicationExpression(AbstractExpression):
    """ 
    Non-Terminal Expression
    """
    def __init__(self, left: Number, right: Number) -> None:
        """ 
        :param left: left part of expression
        :param right: right part of expression
        """
        self.left = left
        self.right = right
    
    
    def interpret(self) -> int | float:
        """ 
        :returns: return multiplication of left and right part
        """
        return self.left.interpret() * self.right.interpret()


class DivisionExpression(AbstractExpression):
    """ 
    Non-Terminal Expression
    """
    def __init__(self, left: Number, right: Number) -> None:
        """ 
        :param left: left part of expression
        :param right: right part of expression
        """
        self.left = left
        self.right = right
    
    
    def interpret(self) -> int | float:
        """ 
        :returns: return division of left and right part
        """
        return self.left.interpret() / self.right.interpret()


class AdditionExpression(AbstractExpression):
    """ 
    Non-Terminal Expression
    """
    def __init__(self, left: Number, right: Number) -> None:
        """ 
        :param left: left part of expression
        :param right: right part of expression
        """
        self.left = left
        self.right = right
    
    
    def interpret(self) -> int | float:
        """ 
        :returns: return addition of left and right part
        """
        return self.left.interpret() + self.right.interpret()


class SubtractionExpression(AbstractExpression):
    """ 
    Non-Terminal Expression
    """
    def __init__(self, left: Number, right: Number) -> None:
        """ 
        :param left: left part of expression
        :param right: right part of expression
        """
        self.left = left
        self.right = right
    
    
    def interpret(self) -> int | float:
        """ 
        :returns: return subtraction of left and right part
        """
        return self.left.interpret() - self.right.interpret()


class Context(object):
    """ 
    Parse string and create the abstract syntax tree
    """
    def evaluate(self, line: str) -> bool:
        """ 
        Analyze and parse string
        
        :param line: line from user for analyze
        :returns: return True if line equals 'exit', False otherwise
        """
        line = line.strip()
        
        if line == 'exit':
           return True
        
        elements = line.split()
        elements = Context.check_elements(elements)
        sequence_of_operations = ['**', '*', '/', '+', '-']
        for operator in sequence_of_operations:
            operator_count = elements.count(operator)
            for _ in range(operator_count):
                index_of_operator = elements.index(operator)
                index_operand_1, index_operand_2 = index_of_operator - 1, index_of_operator + 1
                left, right = Number(elements[index_operand_1]), Number(elements[index_operand_2])
                result = Context.make_operation(left, operator, right)
                for i in range(index_operand_2, index_operand_1 - 1, -1):
                    elements.pop(i)
                elements.insert(index_operand_1, str(result))
                print('=', *elements)
        
        if len(elements) > 1:
            raise IndexError
        
        return False
    
    
    @staticmethod
    def check_elements(elements: list) -> list:
        """
        Check first element and length elements for valid
        
        :param elements: list of elements
        :returns: return list of elements without first element
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
        """
        Make operation with left and right part of expression by operator
        
        :param left: left part of expression
        :param operator: operator of expression
        :param right: right part of expression
        :returns: return result of expression
        """
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
        
        return result
        

for line in stdin:
    flag_exit = False
    try:
        flag_exit = Context().evaluate(line)
    except IndexError:
        print('Проверьте строку, которую Вы ввели.')
    except ZeroDivisionError:
        print('Нельзя делить на 0')
    except ValueError:
        print('Вы пытаетесь выполнить математическую операцию не с числом')
    
    if flag_exit:
         break