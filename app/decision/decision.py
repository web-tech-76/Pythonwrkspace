def __simple_if_loop__(var: int):

    if var > 0:
        if var < 100:
            print("value is not hundred the value is %s" % var)
        elif var == 100:
            print("value is in special {}".format(var))

        else:
            print("the value is greater than hundred {n}".format(n=var))

    else:
        print("value is negative:-  {0}".format(var))

    return


def __simple_pass_block(letter):
    if letter == 'h':
        pass
        print("pass block")

    print("the letter is {c}".format(c=letter))
    return
