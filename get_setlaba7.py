class Person:
    def __init__(self, name, age, gender):
        self._name = name
        self._age = age
        self._gender = gender

    def get_name(self):
        return self._name

    def set_age(self, name):
        self._name = name

    def get_age(self):
        return self._age

    def set_name(self, age):
        self._age = age

    def get_name(self):
        return self._gender

    def set_name(self, gender):
        self._gender = gender


person = Person("Botik", "4", "female")
print(person._name)
print(person._age)
print(person._gender)