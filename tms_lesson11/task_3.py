""" 
2. Написать класс Iterator, который принимает необязательный параметр start_year: int -
начальный год, который по умолчанию равен году вашего рождения, и при передаче
объекта этого класс в for, он может бесконечно возвращать объекты класса Birthday,
который, в свою очередь, при передаче в print возвращает "<год> <день недели>".

bd_iter = Iterator(2006)
for bd in bd_iter:
    print(bd)

# 2006 вторник
# 2007 среда
# ...
"""


class Iterator(object):
    def __init__(self, start_year: int = 1997) -> None:
        self.start_year = start_year
    
    
    def __iter__(self):
        return self
    
    
    def __next__(self):
        birthday = Birthday(self.start_year)
        self.start_year += 1
        return birthday


class Birthday(object):
    def __init__(self, year: int, month: int = 7, day: int = 5) -> None:
        self.year = year
        self.month = month
        self.day = day
    
    
    def weekday_from_date(self) -> int:
        year, month, day = self.year, self.month, self.day 
        if (month == 1 or month == 2):
            year -= 1
            
        month = month - 2
        if month <= 0:
            month += 12
        c = year // 100
        year = year - c * 100
            
        weekday = (day + ((13 * month - 1) // 5) + year + (year // 4 + c // 4 - 2 * c + 777)) % 7
        return weekday
    
    
    def __str__(self) -> str:
        day = self.weekday_from_date()
        return f"{self.year} {days_of_week[day]}"
    

days_of_week = ['воскресенье', 'понедельник', 'вторник', 'среда', 'четверг', 'пятница', 'суббота']
bd_iter = Iterator(2006)
for bd in bd_iter:
    print(bd)