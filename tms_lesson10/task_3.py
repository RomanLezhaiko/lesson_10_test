""" 
3. Ввести уровень абстракции в текущую реализацию добавив классы TerminalExpression с
обязательным аргументом value: float, представляющий значения, которые нельзя разбить
на части - это числа, класс Number должен быть унаследован от этого класса,
NonTerminalExpression с двумя обязательными аргументами left - левый операнд, right
- правый операнд, который будет представлять любое комплексное выражение, т.е все
классы операций Add, ..., Pow должны быть унаследованы от этого класса. И последним
мы добавим класс AbstractExpression, который будет представлять любое выражение в программе,
и который будет иметь только один абстрактный метод(смотреть @abc.abstractmethod) - interpret()
возвращающий вычисленное значение float. Классы TerminalExpression и NonTerminalExpression 
должны быть унаследованы от него.
"""
from abc import abstractmethod


class AbstractExpression(object):
    """ 
    All Terminal and Non-Terminal expressions will implement an interpret method
    """
    @abstractmethod
    def interpret(self):
        pass


class TerminalExpression(AbstractExpression):
    def __init__(self, value: float) -> None:
        self.value = value
    
    
    def interpret(self):
        return self.value


class NonTerminalExpression(AbstractExpression):
    def __init__(self, left, right) -> None:
        self.left = left
        self.right = right
    
    
    def interpret(self):
        pass
