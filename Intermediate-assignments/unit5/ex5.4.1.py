def func(num1, num2):
    """
    The function returns the average of the numbers
    :param num1: int number
    :param num2: int number
    :return: average of the two params
    """
    avg = (num1 + num2) / 2
    return avg


def main():
    # Call the function func
    result = func(5, 9)
    print("The average is:", result)
    # Print the documentation of func
    help(func)


if __name__ == "__main__":
    main()
