import dis


def with_loop():
    result = []
    for i in range(10):
        result.append(i)
    return result


def with_comprehension():
    return [i for i in range(10)]


if __name__ == "__main__":
    print(dis.dis(with_loop))
    print("_____________________")
    print("\n" * 3)
    print(dis.dis(with_comprehension))