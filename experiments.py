# Animal class yarating.
# Method:
# speak()
# Keyin:
# Dog
# Cat
# classlari Animal dan meros olsin.
# Vazifa:
# Har biri speak() methodini o‘ziga mos qilib override qilsin.

class Animal:
    def __setattr__(self, key, value):
        if key == 'Dog':
            print(True)
        else:
            print(False)
    def speak(self):
        print('speak')
        return f"This animal is making a sound"
class Dog(Animal):
    pass
class Cat(Animal):
    pass
dog = Dog()
cat = Cat()
print(dog.speak())
print(cat.speak())