class Cat:
    amount_of_cats = 0
    def __init__(self, name="Безіменний", age=1):
        self.name = name
        self.age = age
        Cat.amount_of_cats += 1
    def meow(self):
        print(f"{self.name} каже: Мяу!")
    def sleep(self):
        print(f"{self.name} спить.")
    def eat(self):
        print(f"{self.name} їсть.")
cat1 = Cat("Мортік", 2)
cat2 = Cat("Муська", 1)
cat1.meow()
cat2.sleep()
print(cat1.amount_of_cats)
print(cat2.amount_of_cats)