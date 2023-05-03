BIG_SIZE = 5
SMALL_SIZE = 1


def chocolate_maker(small, big, x):
    if (small * SMALL_SIZE + big * BIG_SIZE) >= x:
        return True
    else:
        return False
