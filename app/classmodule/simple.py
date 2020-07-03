# from typing import Generic
# from logging import Logger


class Show:
    __value = 0.00
    __fact_value = 0.00

    @classmethod
    def __init__(cls):
        cls.__value = 0.00
        cls.__fact_value = 0.00
        return


    @classmethod
    def func_print(cls, val):
        cls.__value = val
        print("value printing from class ", cls.__value)
        return


    @classmethod
    def __factorial__(cls, value):
        if value == 1:
            return 1
        else:
            return value * cls.__factorial__(value - 1)


    @classmethod
    def __add_values__(cls, *value) -> float:
        __sum = cls.__value

        for i in value:
            __sum += i

        cls.func_print(__sum)

        return __sum
