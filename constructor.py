# _____________________________________
# コンストラクタとデストラクタ
# _____________________________________


class sample_class:
    # コンストラクタ
    def __init__(self, msg, name=None):
        print('コンストラクタが呼ばれました')
        self.msg = msg    # インスタンス変数
        self.name = name  # インスタンス変数

    # デストラクタ
    def __del__(self):
        print('デストラクタが実行されました')
        print('name = {}'.format(self.name))

    def print_msg(self):
        print(self.msg)

    def print_name(self):
        print(self.name)


# インスタンス化
var_1 = sample_class('Hellow', 'Taro')

var_1.print_msg()
var_1.print_name()

# インスタンスの削除
del var_1

'''
コンストラクタが呼ばれました
Hellow
Taro
デストラクタが実行されました
name = Taro
'''
