import pytest

def multi(x, y):
    return x * y

def test_multiply():
    assert multi(2, 3) == 6
    assert multi(-1, 5) == -5
    assert multi(0, 100) == 0



if __name__ == "__main__":
    print("Hello")

    n = int(input("Please enter a number for the loop: "))
    for i in range(n+1):
        print(i, end=",") if i < n else print(i)

    a, b = 2, 3
    x = multi(a, b)
    print(x)
