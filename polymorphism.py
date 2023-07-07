# _____________________________________
# ポリモフィズム(多態性)
# 実行される際にどのクラスのインスタンスかが決定されて実行する
# _____________________________________

from abc import ABCMeta, abstractclassmethod


class Animals(metaclass=ABCMeta):  # type(デフォルトのメタクラス)

    # コンストラクタ
    def __init__(self, name):
        self.name = name

    @abstractclassmethod
    def say_something(self):
        pass

    def say_name(self):
        print(f"My name is {self.name}")


class Woman(Animals):

    def say_something(self):
        print(f"My name is {self.name}. 女性の方です")


class Man(Animals):

    def say_something(self):
        print(f"My name is {self.name}. 男性の方です")


# ポリモーフィズム
num = input('0か1を入力してください')
if num == '0':
    Animals = Man('Taro')
elif num == '1':
    Animals = Woman('Hanako')
else:
    print('入力が正しくありません。0か1を入力してください')

Animals.say_something()

'''
0か1を入力してください0
My name is Taro. 男性の方です

0か1を入力してください1
My name is Hanako. 女性の方です
'''


# class Animals(metaclass=ABCMeta):  # type(デフォルトのメタクラス)

#     @abstractclassmethod
#     def say_something(self):
#         pass

#     def speaks(self):
#         pass


# class Dog(Animals):

#     def say_something(self):
#         print("ワン！")


# class Cat(Animals):

#     def say_something(self):
#         print("にゃー！")


# class Sheep(Animals):

#     def say_something(self):
#         print("めぇぇぇ！")


# class Other(Animals):

#     def say_something(self):
#         print("指定された動物は存在しません")


# # ポリモーフィズム
# num = input('好きな動物は？ 1:犬, 2:猫, 3:羊')
# if num == '1':
#     Animals = Dog()
# elif num == '2':
#     Animals = Cat()
# elif num == '3':
#     Animals = Sheep()
# else:
#     Animals = Other()

# Animals.say_something()

# '''
# 好きな動物は？ 1:犬, 2:猫, 3:羊 2
# にゃー！
# '''
