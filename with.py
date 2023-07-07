# _____________________________________
# with
# _____________________________________


# その2

class WithTest:
    # コンストラクタ
    def __init__(self, file_name):
        print('init called!')
        self.__file_name = file_name

    def __enter__(self):
        print('enter called!')
        self.__file = open(self.__file_name, mode='w', encoding='utf-8')
        return self

    def write(self, msg):
        self.__file.write(msg)

    def __exit__(self, exc_type, exc_val, traceback):
        # 引数の名前は他でも問題ないが一般的に決まっている
        # エラーハンドリングのために存在している
        print('exit called!')
        self.__file.close()


with WithTest('./resorces/output.txt') as t:
    print('withの中')
    t.write('サンプルテキスト')

'''
init called!
enter called!
withの中
exit called!
'''
