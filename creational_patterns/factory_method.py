from abc import ABC, abstractmethod


class IProduct(ABC):

    @abstractmethod
    def release(self):
        pass


class Car(IProduct):
    def release(self):
        print("Car Released")


class Truck(IProduct):
    def release(self):
        print('Truck Released')


class IWorkShop(ABC):

    @abstractmethod
    def create(self) -> IProduct:
        pass


class CreateCar(IWorkShop):
    def create(self) -> Car:
        return Car()


class CreateTruck(IWorkShop):
    def create(self) -> Truck:
        return Truck()


if __name__ == '__main__':
    creator = CreateCar()
    car = creator.create()

    creator = CreateTruck()
    truck = creator.create()

    car.release()
    truck.release()
