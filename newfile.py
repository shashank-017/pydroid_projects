class sk:
    def __init__(self, name, age):
        self.name=name
        self.age=age
    def display_name(self):
        print(f"Your name is: {name}\n")
    def display_age(self):
        print(f"Your age is: {age}")
        if age>=18:
            print('You\'re adult')
        else:
            print('You\'re kid')
name=input('Enter your name\n')
age=int(input('Enter your age\n'))
obj=sk(name,age)
obj.display_name()
obj.display_age()