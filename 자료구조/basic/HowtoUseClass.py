#파이썬은 객체지향 프로그래밍(OOP, Object Oriented Programming)을 기본적으로 지원하고 있다.
# 클래스는 데이타를 표현하는 속성(attribute)과 행위를 표현하는 메서드(method)를 포함하는 논리적인 컨테이너

# Python 클래스는 기본적으로 모든 멤버가 public이다. 접근 제한자가 없다.
class Rectangle:
    # 클래스 정의에서 메서드 밖에 존재하는 변수를 클래스 변수(class variable)라 하는데,
    # 이는 해당 클래스를 사용하는 모두에게 공용으로 사용되는 변수이다.
    # 클래스 변수는 클래스 내외부에서 "클래스명.변수명" 으로 엑세스 할 수 있다.
    cnt=0

    def __init__(self,width,height):
        print("class Initializer")
        self.width=width
        self.height=height
        Rectangle.cnt+=1

    def calcArea(self):
        return self.width*self.height

    # Special Method (Magic Method)
    def __cmp__(self, other):
        return self.width*self.height<=other


#파이썬은 객체지향 프로그래밍의 상속(Inheritance)을 지원하고 있다.
#클래스를 상속 받기 위해서는 파생클래스(자식클래스)에서 클래스명 뒤에 베이스클래스(부모클래스) 이름을 괄호와 함께 넣어 주면 된다.

class Animal:
    def __init__(self,name):
        self.name=name
    def eat(self):
        print("eating")
    def introduce(self):
        print("I am animal. call me "+self.name)

#파이썬은 복수의 부모클래스로부터 상속 받을 수 있는 Multiple Inheritance를 지원하고 있다(animal -> dog, bird)
#파생클래스는 베이스클래스의 멤버들을 호출하거나 사용할 수 있으며
class Dog(Animal):
    def introduce(self):
        print("I am dog. call me "+self.name)

class Bird(Animal):
    def introduce(self):
        print("I am bird. call me "+self.name)

if __name__ == '__main__':
    print(Rectangle.cnt)
    # 하나의 클래스로부터 여러 객체 인스턴스를 생성해서 사용할 수 있다.
    # 클래스 변수가 하나의 클래스에 하나만 존재하는 반면, 인스턴스 변수는 각 객체 인스턴스마다 별도로 존재한다.
    # 메서드 안에서 사용되면서 "self.변수명"처럼 사용되는 변수를 인스턴스 변수(instance variable)라 하는데,
    # 이는 각 객체별로 서로 다른 값을 갖는 변수이다.
    # 인스턴스 변수는 클래스 내부에서는 self.width 과 같이 "self." 을 사용하여 엑세스하고,
    # 클래스 밖에서는 "객체변수.인스턴스변수"와 같이 엑세스 한다.

    #파이썬에서 인스턴스를 생성하기 위해서는 "객체변수명 = 클래스명(입력파라미터들)"과 같이 클래스명을 함수 호출하는 것처럼 사용하면 된다.

    r=Rectangle(2,3)
    print(r.calcArea())
    print(Rectangle.cnt)

    # dog= Dog("bom")
    # dog.introduce()

    animals =[Dog("chiwawa"),Bird("crow"),Bird("chicken")]
    for a in animals:
        a.introduce()
#참고 : http://pythonstudy.xyz/python/article/19-%ED%81%B4%EB%9E%98%EC%8A%A4