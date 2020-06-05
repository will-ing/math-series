

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


# researched from https://www.geeksforgeeks.org/lucas-numbers/

def lucas(v):
    """
    Returns the value of v in the lucas sequence.

    arg() = integer
    """
    first = 2
    second = 1

    if v == 0:
        return first

    for i in range(2, v + 1):
        sum_of = first + second
        first = second
        second = sum_of
    return second


def sum_series(v, first=0, second=1):
    """
     The required parameter will determine which element
     in the series to print.The two optional parameters
     will have default values of 0 and 1 and will determine
     the first two values for the series to be produced.

     arg() = integer
     1st arg = index
     2nd arg = start value
     3rd arg = second value
    """
    if v < 0:
        print("Try Again!")
    elif v == 0 and first == 2 and second == 1:
        return 2
    elif v == 1 and first == 2 and second == 1:
        return 1
    elif v == 0:
        return 0
    elif v == 1:
        return 1
    else:
        v - 1
        return (sum_series(v - 1, first, second) +
                sum_series(v - 2, first, second))
