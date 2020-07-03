def __iterate_obj__():
    items: tuple = (1, 2, 3, 4, 5)

    item_iter = iter(items)

    # range_list = create_range()

    for i in items:
        print("value: ", item_iter.__next__())

        # print("value: ", next(item_iter))
        # print("tuple iter" , next(items))

        # for i in range_list:
        #     print("range values %s " % i)
    return


def create_prime_range(min_num: int, max_num: int):
    if (max_num > 1 and min_num > 1) and (max_num > min_num):
        for num in range(min_num, max_num):
            for index in range(2, num//2):
                if num % index == 0:
                    # print(num, "is not prime number ")
                    break
            else:
                print(num, "is prime number" )
    else:
        print("please provide valid lower and higher range" )
    return


def create_square_seq(min_num: int, max_num: int):
    range_local_list = range(min_num, max_num)
    for index in range_local_list:
        yield index * index
        return
