import time
import os


def pi_digits(x):
    k, a, b, a1, b1 = 2, 4, 1, 12, 4
    while x > 0:
        p, q, k = k * k, 2 * k + 1, k + 1
        a, b, a1, b1 = a1, b1, p*a + q*a1, p*b + q*b1
        d, d1 = a/b, a1/b1
        while d == d1 and x > 0:
            yield int(d)
            x -= 1
            a, a1 = 10*(a % b), 10*(a1 % b1)
            d, d1 = a/b, a1/b1


number_of_digits = int(input("Enter number of digits of pi to compute: "))

start = time.time()
digits = [str(n) for n in list(pi_digits(number_of_digits))]
time = time.time() - start
print("%s.%s\n" % (digits.pop(0), "".join(digits)))
print(f"Calculated in {time}")
