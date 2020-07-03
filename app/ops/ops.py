temp_list = ["abed", 786, 2.23, "john", 70.2]


def string_ops(str_val: str):
    print(str_val)
    print(str_val[1:])
    print(str_val[2:4])
    print(str_val[:5])
    print(str_val * 2)
    print(str_val + "test")
    pass


def list_ops():
    num_list: list = [1, 2, 3, 4]
    print("temp list : - ", temp_list)
    print("num list : 1-3 ", num_list[1:3])
    print("temp list till 2 : - ", temp_list[:2])
    print("temp list from 1 : - ", temp_list[1:])
    print("concat both lists: - ", temp_list + num_list)
    pass


def tuples_ops():
    simple: tuple = (1, 2, '', 4)
    tiny: tuple = ('1', 'a', "jedd", 100, 344.34)
    print("simple tuple:  ", simple)
    print("simple tuple till 1:  ", simple[:1])
    print("concat tuples:  ", (simple + tiny))
    print("tiny tuple [2:4]  ", tiny[2:4])
    print("in operator ", 344.34 in tiny)
    pass


def sum_num(a: int, b: int):
    c: int = 0
    c = a + b
    return c


"""

"""


# ________________________________________________________________________________
def display():
    print(' I am in display')
    print(' sum is ', sum_num(10, 20))
    print(' subtraction of nums is ', subtract_num(3089, 8345))
    pass


# ________________________________________________________________________________
def subtract_num(a: int, b: int):
    return a - b
    pass
