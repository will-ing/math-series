

def fibonacci(v):
    """
    Returns the value of v in the fibonacci sequence.

    arg() = integer
    """

    if v < 0:
        print("Try Again!")
    elif v == 0:
        return 0
    elif v == 1:
        return 1
    else:
        v - 1
        return fibonacci(v - 1) + fibonacci(v - 2)


def lucas(v):
    """
    Returns the value of v in the lucas sequence.

    arg() = integer
    """
    first = 2
    second = 1

    if (v == 0):
        return first

    for i in range(2, v + 1):
        sum_of = first + second
        first = second
        second = sum_of

    return second
