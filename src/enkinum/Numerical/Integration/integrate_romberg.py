def integrate_romberg(f, a, b, n=5):
    """
    Romberg's method for definite, single dimension integrals.
    Error of O(h_n^(2n + 2))

    :param f: function to be evaluated
    :param a: lower bound of definite integral
    :param b: upper bound of definite integral
    :param n: number of rows and columns of Romberg Array to create (default n = 5)

    :return: Double-precision float of estimated value.
    """
    h = b - a
    rom_matrix = [[0 for x in range(n)] for y in range(n)]
    rom_matrix[0][0] = (h/2) * (f(a) + f(b))
    for i in range(n):
        h = h / 2
        sum = 0
        for k in range(1,n,2):
            sum = sum + f(a + (k * h))
        rom_matrix[i][0] = 0.5 * rom_matrix[i-1][0] + (sum * h)
        for j in range(i):
            rom_matrix[i][j] = rom_matrix[i][j-1] + (rom_matrix[i][j-1] - rom_matrix[i-1][j-1])/((4 ** j) - 1)
    return rom_matrix[n][n]
