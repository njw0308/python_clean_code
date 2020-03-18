class Person:

    def __init__(self, name, age):
        self._name = name
        self._age = age
    
    @property
    def name(self):
        """
        이름 출력
        """
        return self._name
    
    @property
    def age(self):
        """
        나이 출력
        """
        return self._age
    
    def personal_info(self):
        return "이름 : {} , 나이 - {}".format(self._name, self._age)
    

class Student(Person):
    """
    학생
    """
    
    def __init__(self, name, age, student_id):
        #Person.__init__(self, name, age)
        super().__init__(name, age)
        self._student_id = student_id
    
    @property
    def student_id(self):
        return self._student_id

    def personal_info(self):
        return "이름 : {}, 나이 : {}, 학생 번호 : {}".format(self._name, self._age, self._student_id)

class UniversityStudent(Student):
    """
    대학생
    """

    def __init__(self, name, age, student_id):
        super().__init__(name, age, student_id)
    
    def personal_info(self):
        return "이름 : {}, 나이 : {}, 학생 번호 : {}, 대학생 : True".format(self._name, self._age, self._student_id)

Doo = Person('doo', 3)
Joo = Student('joo', 2, '38')
Joo2 = UniversityStudent('joo2', 21, '12')

print(Doo.age, Doo.name, Doo.personal_info())
print(Joo.age, Joo.name, Joo.student_id, Joo.personal_info())
print(Joo2.age, Joo2.name, Joo2.student_id, Joo2.personal_info())
