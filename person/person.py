# Python 에서는 기본적으로 클래스 객체가 public 이다.. 함수도 다 보임!
class Person:
    # 멤버 변수 같은 것들은 제알 상단에다가 정의하고 사용하면 된다.
    numPerson = 0
    title = "MR"
    def __init__(self):
        self.firstName = "John"
        self.lastName = "Doe"
        Person.numPerson += 1

    def print(self):
        print("Hello. My name is {0} {1}".format(self.firstName, self.lastName))


p1 = Person()
p1.firstName = "Vince"
p1.lastName = "Carter"
p1.print()

p2 = Person()
print(Person.numPerson)



# Runtime 실행시간
print(p1.title)
print(p2.title)
Person.title = "MS"
print(Person.title)
