class House():

    def __init__(self, name=None, num_of_floors=None):
        self.name = name
        self.number_of_floors = num_of_floors

    def go_to(self, new_floor):
        if 0 < new_floor <= self.number_of_floors:
            print(new_floor)
        else:
            print(f"Такого этажа не существует {new_floor} ")


home = House(name="ЖК Эльбрус", num_of_floors=30)
home.go_to(31)
