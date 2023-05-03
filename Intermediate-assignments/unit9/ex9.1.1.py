def are_files_equal(file1, file2):
    f1 = open(file1, "r")
    f2 = open(file2, "r")
    for line in f1:
        if line != f2.readline():
            f1.close()
            f2.close()
            return False
    f1.close()
    f2.close()
    return True
