def own_zip(l1, l2):
    for i, el in enumerate(l1):
        yield (el, l2[i])


def main():
    list1 = [x ** 2 for x in range(20)]
    list2 = [x ** 2 for x in range(25)]
    res1 = list(own_zip(list1, list2))
    res2 = list(own_zip(list2, list1))

    for (a1, b1), (b2, a2) in own_zip(res1, res2):
        assert a1 == a2
        assert b1 == b2


if __name__ == "__main__":
    main()
