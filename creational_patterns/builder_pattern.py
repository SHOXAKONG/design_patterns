from abc import ABC, abstractmethod


class Phone:
    def __init__(self):
        self.data: str = ''

    def about_phone(self) -> str:
        return self.data

    def append_data(self, data: str):
        self.data += data


class IDeveloper(ABC):

    @abstractmethod
    def create_display(self):
        pass

    @abstractmethod
    def create_box(self):
        pass

    @abstractmethod
    def system_install(self):
        pass

    @abstractmethod
    def get_phone(self) -> Phone:
        pass

class AndroidDeveloper(IDeveloper):
    def __init__(self):
        self.__phone = Phone()

    def create_display(self):
        self.__phone.append_data('Samsung Display created; ')

    def create_box(self):
        self.__phone.append_data("Samsung Box created; ")

    def system_install(self):
        self.__phone.append_data('Installed Android System')

    def get_phone(self) -> Phone:
        return self.__phone

class IOSDeveloper(IDeveloper):
    def __init__(self):
        self.__phone = Phone()

    def create_display(self):
        self.__phone.append_data('Iphone Display created; ')

    def create_box(self):
        self.__phone.append_data("Iphone Box created; ")

    def system_install(self):
        self.__phone.append_data('Installed IOS System')

    def get_phone(self) -> Phone:
        return self.__phone

class Director:
    def __init__(self, developer: IDeveloper):
        self.__developer = developer

    def set_developer(self, developer: IDeveloper):
        self.__developer = developer

    def mount_only_phone(self) -> Phone:
        self.__developer.create_box()
        self.__developer.create_display()

        return self.__developer.get_phone()

    def mount_full_phone(self) -> Phone:
        self.__developer.create_box()
        self.__developer.create_display()
        self.__developer.system_install()

        return self.__developer.get_phone()


if __name__ == '__main__':
    android_developer: IDeveloper = AndroidDeveloper()
    ios_developer: IDeveloper = IOSDeveloper()

    director = Director(android_developer)
    samsung: Phone = director.mount_full_phone()
    print('Samsung -> ' + samsung.about_phone())

    director.set_developer(ios_developer)
    iphone: Phone = director.mount_full_phone()
    print('Iphone -> ' + iphone.about_phone())
