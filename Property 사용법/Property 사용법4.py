class Person:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    #기존의 get_age에서 get_을 삭제한다
    @property
    def age(self):
        return self._age

    #기존의 set_age 에서 set_을 삭제하고 .setter를 붙여준다
    @age.setter
    def age(self, age):
        if age < 0:
            raise ValueError("Invalid age")
        self._age = age

person = Person("John", "Doe", 20)
person.age