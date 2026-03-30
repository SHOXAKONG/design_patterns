import copy

class Animal:
    __name: str = ''
    __params: dict = {
        "Height": 183,
        "Weight": 80
    }

    def __init__(self, donor: 'Animal' = None):
        if donor is not None:
            self.__name = donor.get_name()
            self.__params = copy.deepcopy(donor.get_params())


    def set_name(self, name: str):
        self.__name = name

    def get_name(self) -> str:
        return self.__name

    def get_params(self) -> dict:
        return self.__params

    def set_weight(self, new_weight: int):
        self.__params['Weight'] = new_weight

    def clone(self):
        return Animal(self)

if __name__ == '__main__':
    animal_donor: Animal = Animal()
    animal_donor.set_name('John')


    animal_clone: Animal = animal_donor.clone()

    print("Donor Animal: ", animal_donor.get_name(), animal_donor.get_params())
    print("Clone Animal: ", animal_clone.get_name(), animal_clone.get_params())


    animal_clone.set_weight(100)
    animal_clone.set_name('New John')
    print()

    print("Donor Animal: ", animal_donor.get_name(), animal_donor.get_params())
    print("Clone Animal: ", animal_clone.get_name(), animal_clone.get_params())

