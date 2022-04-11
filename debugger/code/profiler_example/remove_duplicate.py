from random import randint


def visited():
    return []


def not_seen(vis, value):
    if value not in vis:
        vis.append(value)
        return True
    return False


def test_remove_duplicate():
    res = []
    vis = visited()
    for el in (randint(0, 10000) for _ in range(10000)):
        if not_seen(vis, el):
            res.append(el)

    print(f"found {len(res)} unique elements")


if __name__ == "__main__":
    test_remove_duplicate()
