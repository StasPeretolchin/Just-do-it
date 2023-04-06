"""
Задача на программирование повышенной сложности: огромное число Фибоначчи по модулю

Даны целые числа 1 ≤ n ≤ 10**18 и 2 ≤ m ≤ 10**5, необходимо найти остаток от деления n-го числа Фибоначчи на m.

https://stepik.org/lesson/13228/step/8?unit=3414
"""


# Мое решение
def pisano_period(m):
    a, b = 0, 1
    period = 0
    for i in range(m * 6):
        a, b = b, (a + b) % m
        if a == 0 and b == 1:
            period = i + 1
            break
    return period


def fib_mod(n, m):
    pisano = pisano_period(m)

    if pisano == 0:
        return n % m
    else:
        n %= pisano
        fib = [0, 1]
        for i in range(2, n+1):
            fib.append((fib[i-1] + fib[i-2]) % m)
        return fib[n]


# Топ решение
def fib_mod_top(n, m):
    o, i = [0, 1], 2
    while not (o[i - 2] == 0 and o[i - 1] == 1) or i <= 2:
        o.append((o[i - 2] + o[i - 1]) % m)
        i += 1
    return o[n % (i - 2)]


def main():
    n, m = map(int, input().split())
    print(fib_mod(n, m))
    print(fib_mod_top(n, m))


if __name__ == "__main__":
    main()

