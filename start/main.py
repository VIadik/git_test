def plus(a: int, b: int):
    return a + b


if __name__ == '__main__':
    a, b = map(int, input().split())
    print(plus(a, b))
