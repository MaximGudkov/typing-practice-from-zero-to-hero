from typing import Protocol


class Drivable(Protocol):
    def drive(self) -> str:
        return "I can drive!!!"


class Driver:
    def drive(self) -> str:
        return "I'm a driver and I can drive!!!"


def take_a_drive(entity: Drivable):
    print(entity.drive())


driver = Driver()
take_a_drive(driver)
