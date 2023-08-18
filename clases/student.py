class Student:
    def __init__(self, name:str,age:int):
        self.name = name
        self.age = age
        self.grade = []

    def add_grade(self, num:float):
        (self.grade).append(num)


