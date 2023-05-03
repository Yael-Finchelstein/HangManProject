def mult_tuple(tuple1, tuple2):
    # first way
    pairs = []
    for i in range(len(tuple1)):
        for j in range(len(tuple2)):
            pairs.append((tuple1[i], tuple2[j]))
            pairs.append((tuple2[j], tuple1[i]))
    return tuple(pairs)

    # second way
    # return tuple((x, y) for x in tuple1 for y in tuple2) + tuple((y, x) for x in tuple1 for y in tuple2)
