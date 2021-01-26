class Person:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

person = Person("Min", "Doe", 2)
print(person.age) #20
print(person.age)
#이렇게 필드명을 사용해서 객체의 내부 데이터에 접근하는 것은 편리하지만,
#해당 데이터는 외부로 부터 무방비 상태에 놓이게 됩니다.