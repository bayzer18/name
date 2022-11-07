class Human:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def calculate_age(self, num):
        self.num = num

    def __str__(self):
        return f'через {self.num} лет, будет {self.age + self.num} лет'

p = Human('kennedy', 46, 'male') 
# print(p)
p.calculate_age(60)
print(p)