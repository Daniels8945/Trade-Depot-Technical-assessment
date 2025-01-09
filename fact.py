def _fac(n: int) -> int:
    """ Takes a positive initiger as input
        Calcultate and return the factorial of the given intiger """
    f = 1
    for i in range(1, n+1):
        f *= i
        print("{:d}".format(f))     
_fac(7)
