""" 
4. *Добавить реализацию последовательного вывода операций.

python calc.py
? 10 * 2 + 3 ** 2
= 10 * 2 + 9
= 20 + 9
= 29

? 2.34 ** 2 - 6 / 0
= 5.4756 - 6 / 0
= Нельзя делить на 0
"""
from __future__ import annotations
from typing import Any
from sys import stdin
from abc import abstractmethod


class AbstractExpression(object):
    """ 
    All Terminal and Non-Terminal expressions will implement an interpret method
    """
    @abstractmethod
    def interpret(self):
        pass


class TerminalExpression(AbstractExpression):
    """ 
    All Terminal expressions must be inherited from this class
    """
    def __init__(self, value: float) -> None:
        self.value = float(value) if '.' in value else int(value)
    
    
    def interpret(self) -> int | float:
        return self.value


class NonTerminalExpression(AbstractExpression):
    """ 
    All Non-Terminal expressions must be inherited from this class
    """
    def __init__(self, left, right) -> None:
        self.left = left
        self.right = right
    
    
    def interpret(self):
        pass


class Number(TerminalExpression):
    def __init__(self, value: str) -> None:
        """ 
        :param value: value is float or int
        """
        super().__init__(value)
    
    
    def interpret(self) -> int | float:
        """ 
        :returns: return value (int or float)
        """
        # print(self.value)
        return self.value


class Add(NonTerminalExpression):
    def __init__(self, left: Any, right: Any) -> None:
        """ 
        :param left: left part of expression
        :param right: right part of expression
        """
        super().__init__(left, right)
    
    
    def interpret(self) -> int | float:
        # print(self.left.__dict__, self.right.__dict__)
        super().interpret()
        return self.left.interpret() + self.right.interpret()


class Sub(NonTerminalExpression):
    def __init__(self, left: Any, right: Any) -> None:
        """ 
        :param left: left part of expression
        :param right: right part of expression
        """
        super().__init__(left, right)
    
    
    def interpret(self) -> int | float:
        super().interpret()
        return self.left.interpret() - self.right.interpret()
    

class Mul(NonTerminalExpression):
    def __init__(self, left: Any, right: Any) -> None:
        """ 
        :param left: left part of expression
        :param right: right part of expression
        """
        super().__init__(left, right)
    
    
    def interpret(self) -> int | float:
        super().interpret()
        return self.left.interpret() * self.right.interpret()


class Div(NonTerminalExpression):
    def __init__(self, left: Any, right: Any) -> None:
        """ 
        :param left: left part of expression
        :param right: right part of expression
        """
        super().__init__(left, right)
    
    
    def interpret(self) -> int | float:
        super().interpret()
        return self.left.interpret() / self.right.interpret()


class Pow(NonTerminalExpression):
    def __init__(self, left: Any, right: Any) -> None:
        """ 
        :param left: left part of expression
        :param right: right part of expression
        """
        super().__init__(left, right)
    
    
    def interpret(self) -> int | float:
        super().interpret()
        return self.left.interpret() ** self.right.interpret()
    
    
class Context(object):
    """
    :attribute op_order: list containing mathematical operators
    """
    op_order = ['+', '-', '*', '/', '**']
    def __init__(self, expression: str) -> None:
        """ 
        :param expression: expression from user input 
        """
        self.expression = expression
        
    
    def _eval(self, substring: str) -> Any:
        """ 
        The method parses the expression into a binary tree, then collects this tree to the top.
        
        :param substring: a string that can be a number or a mathematical expression 
        :returns: return the class represented by a mathematical operation or a number
        """
        substring = substring.strip()
        if substring.isdigit() or substring.replace('.', '', 1).isdigit():
            return Number(substring)
        
        for op in self.op_order:
            if op not in substring:
                continue
            
            parts = substring.split(op, 1)
            
            if op == '+':
                return Add(self._eval(parts[0]), self._eval(parts[1]))
            elif op == '-':
                return Sub(self._eval(parts[0]), self._eval(parts[1]))
            elif op == '*':
                return Mul(self._eval(parts[0]), self._eval(parts[1]))
            elif op == '/':
                return Div(self._eval(parts[0]), self._eval(parts[1]))
            elif op == '**':
                return Pow(self._eval(parts[0]), self._eval(parts[1]))
        
    
    def evaluate(self) -> int | float:
        """ 
        :returns: return result of expression 
        """
        return self._eval(self.expression)


for line in stdin:
    if line.strip() == 'exit':
        break
    
    try:    
        print('=', Context(line).evaluate().interpret())
    except ZeroDivisionError:
        print('Нельзя делить на 0')
    except AttributeError:
        print('Проверьте выражение которое вы ввели.')


# ctx = Context("3*2 + 7^3")
# ctx = Context("3.57657*2.436554 -1 + 7^3")
# ctx = Context("3.57657/0 -1 + 7^3")
# ctx = Context("3.57657/1 -1 + ")
# ctx = Context("3.57657/1 -1 + thytyr")
# ctx = Context(" ")
# ctx = Context("1+ + 1")
