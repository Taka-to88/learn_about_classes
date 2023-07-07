# _____________________________________
# クラスの継承
# _____________________________________


# 親クラス
class Person:
    # コンストラクタ
    def __init__(self, name, age):
        self.name = name  # インスタンス変数
        self.age = age    # インスタンス変数

    def greeting(self):
        print(f"Hellow Sir My name is {self.name}")

    def breathing(self):
        print("su-- ha--")


# 親クラスから継承
class Employee(Person):
    # コンストラクタ
    def __init__(self, name, age, number):
        super().__init__(name, age)
        self.number = number  # インスタンス変数

    def say_number(self):
        print(f'My number is {self.number}')

    def greeting(self):  # オーバーライド（上書き）
        print(f"Hellow Sir My name is {self.name}. number is {self.number}")


# インスタンス化
man = Employee('ジョナサン', 45, '0120-117-117')
man.greeting()


'''
Hellow Sir My name is ジョナサン. number is 0120-117-117
'''
