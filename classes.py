class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors
    def go_to(self, new_floor):
        if new_floor > self.number_of_floors or new_floor < 1:
            print("Введенного этажа не существует")
        else:
            print("Этажи, пройденные вами:")
            for i in range(1, new_floor + 1):
                print(i)

    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        return f"Название: \"{self.name}\", количество этажей: {self.number_of_floors}"


libr = House("Библиотека", 13)
college = House("Колледж", 3)

print(libr)
print(college, '\n')

print(len(libr))
print(len(college))