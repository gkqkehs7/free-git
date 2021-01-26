class Person:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.set_age(age)

    def get_age(self):
        return self._age
    # _로 시작하는 이름을 가진 변수는 외부에서 직접 접근하지 않는다.
    def set_age(self, age):
        if age < 0:
            raise ValueError("Invalid age")
        self._age = age

person = Person("min", "woo", 20)
age = person.get_age()
print(age)
person.age = person.set_age(2)
age = person.get_age()
print(age)

#이렇게 하면 내부 데이터에 대한 접근을 통제할 수 있지만
#기존의 필드명을 바로 사용할 때 보다는 코드가 조금 지저분해진다.