# _____________________________________
# カプセル化、getter、setter
# _____________________________________


# その1

class Human:
    # コンストラクタ
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def get_name(self):
        print('getter_nameを呼び出しました')
        return self.__name

    def get_age(self):
        print('getter_ageを呼び出しました')
        return self.__age

    def set_name(self, name):
        print('setter_nameを呼び出しました')
        self.__name = name

    def set_age(self, age):
        print('setter_ageを呼び出しました')
        self.__age = age

    # nameを指定すると、get_name、set_nameが呼び出される
    name = property(get_name, set_name)
    age = property(get_age, set_age)

    def print_msg(self):
        print(self.name, self.age)


human = Human('Taro', 20)
human.name = 'Jiro'
human.age = 18

print(human.name)
print(human.age)
human.print_msg()

'''
setter_nameを呼び出しました
setter_ageを呼び出しました
getter_nameを呼び出しました
Jiro
getter_ageを呼び出しました
18
getter_nameを呼び出しました
getter_ageを呼び出しました
Jiro 18
'''
