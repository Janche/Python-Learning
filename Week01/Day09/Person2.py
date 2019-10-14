class Person2(object):
    
    # 限定Person对象只能绑定_name, _age和_gender属性
    __slots__ = ('_name', '_age', '_gender')

    def __init__(self, name, age):
        self._name = name
        self._age = age

    @property
    def name(self):
        return self._name

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age):
        self._age = age

    def play(self):
        if self._age <= 16:
            print('%s %s正在玩飞行棋.' % (self._name, self._age))
        else:
            print('%s %s正在玩斗地主.' % (self._name, self._age))


def main():
    person = Person2('王大锤', 22)
    person.play()
    person._gender = '男'
    person._age = 10
    person.play()
    # AttributeError: 'Person' object has no attribute '_is_gay'
    # person._is_gay = True
if __name__ == '__main__':
    main()