class human:
    def __init__(self, name="unknown", age=1,salary=-1):
        self.name = name
        self.age = age
        self.salary = salary

    def greet(self):
        return f"Hello, my name is {self.name} and I am {self.age} years old."

    def introduce(self):
        if self.salary != -1:
            return f"{self.greet()} My salary is {self.salary}."
        return f"{self.greet()} I am not employed."

kishan=human("Kishan", 30, 50000)
kishan_introduction = kishan.introduce()
print(kishan_introduction)

papu=human()
papu.name = "Papu"
papu.age = 25
papu_introduction = papu.introduce()
print(papu_introduction)