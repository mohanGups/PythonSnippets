def nth_root(radicand, n):
    return radicand ** (1/n)


def ordinal_suffix(value):
    s = str(value)
    if s.endswith('11'):
        return 'th'
    elif s.endswith('12'):
        return 'th'
    elif s.endswith('13'):
        return 'th'
    elif s.endswith('1'):
        return 'st'
    elif s.endswith('2'):
        return 'nd'
    elif s.endswith('3'):
        return 'rd'
    return 'th'


def ordinal(value):
    return str(value) + ordinal_suffix(value)


def display_nth_root(radicand, n):
    root = nth_root(radicand, n)
    message = "The " + ordinal(n) + " root of " + \
        str(radicand) + " is " + str(root)
    print(message)


def sqrt(x):
    """Computes square roots using method of Heron
    of Alexandria.

    Args:
        x: The number for which the square root
        is to be computed

    Returns:
        The square root of x.
    """

    if x < 0:
        raise ValueError(
            "Cannot compute square root of "
            f"negative number {x}"
        )

    guess = x
    i = 0
    while guess*guess != x and i < 20:
        guess = (guess + x/guess)/2.0
        i += 1

    return guess


def main():
    print(sqrt(9))
    print(sqrt(2))


if __name__ == '__main__':
    main()
