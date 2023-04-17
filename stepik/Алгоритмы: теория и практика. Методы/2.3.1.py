"""
Задача на программирование: наибольший общий делитель

По данным двум числам 1 ≤ a,b≤ 2⋅10 ** 9 найдите их наибольший общий делитель.

https://stepik.org/lesson/13229/step/5?unit=3415
"""


# Мое решение
def gcd(a, b):
    if a == 0:
        return b
    elif b == 0:
        return a
    elif a >= b:
        return gcd(a % b, b)
    else:
        return gcd(a, b % a)


# Топ решение
def gcd_top(a, b):
    return gcd(b, a % b) if b else a


def main():
    n, m = map(int, input().split())
    print(gcd(n, m))
    print(gcd_top(n, m))


if __name__ == "__main__":
    main()

