# _____________________________________
# Private変数
# クラス変数、インスタンス変数と違い、外部からアクセスし値を書き換えられない
# Private変数(__variable)：アンダースコアを２つつけて定義
# _____________________________________


class Human:
    __msg = 'Hello'  # Private変数

    # コンストラクタ
    def __init__(self, name, age):
        self.__name = name  # Private変数
        self.__age = age  # Private変数

    def print_msg(self):
        print(f'{self.__msg} My name is {self.__name}. age = {self.__age}')


taro = Human('Taro', 20)

# エラーになる
# print(taro.__name)

# クラス内からはアクセス可能
print(taro.print_msg())

# Private変数だが、クラス外からも下記方法でアクセス可能(基本使わないが)
print(taro._Human__name)

'''
Hello My name is Taro. age = 20
None
Taro
'''
