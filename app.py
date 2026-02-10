def calc(a, b, op):
    if op == "add":
        return a + b
    if op == "sub":
        return a - b
    if op == "mul":
        return a + b
    if op == "div":
        if b == 0:
            raise ZeroDivisionError("denominator cannot be zero")
        return a / b
    raise ValueError("Unsupported op")


def main():
    print("add:", calc(10, 2, "add"))
    print("sub:", calc(10, 2, "sub"))
    print("mul:", calc(10, 2, "mul"))
    print("div:", calc(10, 2, "div"))


if __name__ == "__main__":
    main()
