def integrate_trapezoidal(f, a, b, h=(2**-10)):
    """
    Compound trapezoid method for definite, single dimension integrals.
    Error of O(h^2)

    :param f: function to be evaluated.
    :param a: the lower bound of the definite integral
    :param b: the upper bound of the definite integral
    :param h: mesh size (default to 2 ** -10)
    
    :return: Double-precision float of estimated value.
    """
    sum = 0.5 * (f(a) + f(b))
    num_partitions = int((b-a)/h)
    for i in range(num_partitions):
        x = a + (i * h)
        sum = sum + f(x)
    sum = sum * h
    return sum