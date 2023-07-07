# _____________________________________
# クラスの多重継承
# _____________________________________


# 親クラス
class ClassA:
    # コンストラクタ
    def __init__(self, name):
        self.a_name = name  # インスタンス変数

    def print_a(self):
        print("ClassAメソッド実行")
        print(f"A_name is {self.a_name}")

    def print_hi(self):
        print("A hi")


class ClassB:
    # コンストラクタ
    def __init__(self, name):
        self.b_name = name  # インスタンス変数

    def print_b(self):
        print("ClassBメソッド実行")
        print(f"B_name is {self.b_name}")

    def print_hi(self):
        print("B hi")


# 親クラスから継承
class NewClass(ClassA, ClassB):
    # コンストラクタ
    def __init__(self, a_name, b_name, name):
        ClassA.__init__(self, a_name)
        ClassB.__init__(self, b_name)
        self.name = name  # インスタンス変数

    def print_new_name(self):
        print("NewClassメソッド実行")
        print(f'New name is {self.name}')

    def print_hi(self):  # オーバーライド(上書き)
        ClassA.print_hi(self)
        ClassB.print_hi(self)
        print("NewClass hi")


# インスタンス化
sample = NewClass('ジョナサンA', 'ジョナサンB', 'Newジョナサン')
sample.print_a()
sample.print_b()
sample.print_new_name()
sample.print_hi()


'''
ClassAメソッド実行
A_name is ジョナサンA
ClassBメソッド実行
B_name is ジョナサンB
NewClassメソッド実行
New name is Newジョナサン
A hi
B hi
NewClass hi
'''
