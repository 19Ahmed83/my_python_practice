class Mentor:
    def __init__(self, field):
        self.field = field

    def introduce(self):
        return f"I teach {self.field}"


class Student(Mentor):
    pass


learner = Student("Python")
print(learner.introduce())