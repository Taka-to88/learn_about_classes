# _____________________________________
# カプセル化、getter、setter
# @property, @var.setter
# _____________________________________


# その2

class Human:
    # コンストラクタ
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    @property
    def name(self):
        print('getter_nameを呼び出しました')
        return self.__name

    @property
    def age(self):
        print('getter_ageを呼び出しました')
        return self.__age

    @name.setter
    def name(self, name):
        print('setter_nameを呼び出しました')
        self.__name = name

    @age.setter
    def age(self, age):
        print('setter_ageを呼び出しました')
        if age < 0:
            print('0以上の値を設定してください')
            return
        self.__age = age


human = Human('Taro', 20)
human.name = 'Jiro'
human.age = -1

print(human.name)
print(human.age)

'''
setter_nameを呼び出しました
setter_ageを呼び出しました
0以上の値を設定してください
getter_nameを呼び出しました
Jiro
getter_ageを呼び出しました
20
'''
