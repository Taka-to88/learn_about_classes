# _____________________________________
# メタクラス
# メタクラスを作成すると、クラスを作成した際にそのクラス自体を再定義して、
# 値の検証のような用途に使用できます。
# _____________________________________

# 例外を自分で定義
class MetaException(Exception):
    pass


class Meta1(type):  # type(デフォルトのメタクラス)
    print('パターン1_____________________________________')

    # コンストラクタ
    def __new__(metacls, name, bases, class_dict):
        print(f"metacls is {metacls}")
        print(f"name is {name}")
        print(f"bases is {bases}")  # 継承しているクラス
        print(f"class_dict is {class_dict}")
        if 'my_var' not in class_dict.keys():
            raise MetaException('my_varを定義してください')
        return super().__new__(metacls, name, bases, class_dict)


class ClassA(metaclass=Meta1):
    a = '123'
    my_var = 'AAA'
    pass


# 継承したく無いクラスを作成する場合等に利用することができる
# このクラスで完結


class Meta2(type):  # type(デフォルトのメタクラス)
    print('パターン2_____________________________________')

    # コンストラクタ
    def __new__(metacls, name, bases, class_dict):
        print(f"metacls is {metacls}")
        print(f"name is {name}")
        print(f"bases is {bases}")  # 継承しているクラス
        print(f"class_dict is {class_dict}")
        for base in bases:
            if isinstance(base, Meta2):
                raise MetaException('継承できません')  # finalクラス

        return super().__new__(metacls, name, bases, class_dict)


class ClassB(metaclass=Meta2):
    a = '123'
    my_var = 'AAA'
    pass


class SubClaseeB(ClassB):
    pass


'''
パターン1_____________________________________
metacls is <class '__main__.Meta1'>
name is ClassA
bases is ()
class_dict is {'__module__': '__main__', '__qualname__': 'ClassA', 'a': '123', 'my_var': 'AAA'}
パターン2_____________________________________
metacls is <class '__main__.Meta2'>
name is ClassB
bases is ()
class_dict is {'__module__': '__main__', '__qualname__': 'ClassB', 'a': '123', 'my_var': 'AAA'}
metacls is <class '__main__.Meta2'>
name is SubClaseeB
bases is (<class '__main__.ClassB'>,)
class_dict is {'__module__': '__main__', '__qualname__': 'SubClaseeB'}
Traceback (most recent call last):
  File "/Users/takatokondou/study/meta_class.py", line 58, in <module>
    class SubClaseeB(ClassB):
  File "/Users/takatokondou/study/meta_class.py", line 47, in __new__
    raise MetaException('継承できません')  # finalクラス
__main__.MetaException: 継承できません
'''
