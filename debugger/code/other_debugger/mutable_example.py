def create_list(a, b, initial=[]):
    initial.extend([a, b])
    return initial


def main():
    assert len(create_list(1, 2, [])) == 2
    assert len(create_list(1, 2)) == 2
    assert len(create_list(1, 2)) == 2


if __name__ == "__main__":
    main()
