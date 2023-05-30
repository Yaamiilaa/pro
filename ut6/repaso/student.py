from random import randint


class Student:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
        self.registration = randint(1000, 10000)
        self.notes = []

    def add_note(self, note: int):
        self.notes.append(note)

    @staticmethod
    def get_avg_notes(self) -> int:
        return sum(self.notes) / len(self.notes) if self.notes else 0.0
    
    def __str__(self) -> str:
        return f'''Name: {self.name}
Age: {self.age}
Registration: {self.registration}
Grade point average: {self.get_avg_notes(self)}'''
    

student1 = Student("John Smith", 20)
student2 = Student("Jane Doe", 22)
student1.add_note(80)
student1.add_note(90)
student2.add_note(75)
student2.add_note(85)
student2.add_note(95)
print(student1)
print(student2)