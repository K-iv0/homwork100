from tkinter.font import names


class Car:
    def __init__(self, model, color):
        self.model = model
        self.color = color

    def start(self):
        print(f"{self.color} {self.model} go to")

my_car = Car("BMW", "Red")

class House:
    def __init__(self, name, floors):
        self.name = names
        self.number_floor = floors

    def go_to(self, new_floor):
        if 1 <= new_floor <= self.number_floor:
            for fl in range(1, new_floor + 1):
                print(fl)
            else:
                print("not found")