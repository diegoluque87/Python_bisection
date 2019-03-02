# ***********************************************
# * Program used for the Class of Numerical Methods in Transport Phenomena
# * Numerical Analysis - Burden, Richard - 10th edition - Page 53
# * Algorithm 2.1 - Method of Bisection
# *
# * \param1 Start of the range to be studied
# * \param2 End of the interval to be studied
# * \return Root of the function within the range
# *
# ***********************************************

import math

tol = 1e-15     # minimum tolerance value = 10e-15
n_max = 100     # maximum value for iterations = 100

print('\n' + '=' * 60)
a = float(input("Enter a number to the beginning of the range: "))
b = float(input("Enter a number for the end of the range: "))


def f(x):
    # change your function here

    return pow(x, 3) + 4 * pow(x, 2) - 10
    # return math.sqrt(x) - math.cos(x)
    # return x * 3 - math.exp(x)
    # return (5**x - 5**(-x)) / 2 - 3


def bisection(_a, _b, _tol, _n_max):
    _c = 0
    i: int = 1
    c_previous: float = 0

    while i <= _n_max:
        _c = _a + (_b - _a) / 2
        print(f'i: {i:3} \t a: {_a:.16f} \t b: {_b:.16f} \t c: {_c:.16f} \t f(c): {f(_c):.16f}')
        if f(_a) * f(_c) > 0:
            _a = _c
        else:
            _b = _c
        if math.fabs(_c - c_previous) <= tol and math.fabs(f(_c)) <= tol:
            return _c
        else:
            c_previous = _c
        i = i + 1

    print('\nThe maximum number of iterations has been reached!')
    return _c


if a >= b:
    print("\nError! The value at the beginning of the range must be less than the value at the end of the range.\n")

c = bisection(a, b, tol, n_max)

if math.fabs(f(c)) <= tol:
    print(f'\033[1;34m\nRoot in range [{a:.2f}, {b:.2f}]: {c} \033[m')
else:
    print(f"\033[1;31m\nError! Root function not found in range [{a:.2f}, {b:.2f}] \033[m\n")

print('=' * 60)
