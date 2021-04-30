sequence1 = list(range(0, 51))
sequence2 = list(range(80, 101))
sequence3 = list(range(114, 151))


def checkValue(value: int):
    def checkLessOrGreater(value: int):
        if value < range_median:
            print("it is less than " + str(range_median))
        elif value == range_median:
            pass
        else:
            print("it is greater than " + str(range_median))

    if value in sequence1:
        range_median = sequence1[len(sequence1) // 2]
        print(str(value) + " is in the range 1.")
        checkLessOrGreater(value)
    elif value in sequence2:
        range_median = sequence2[len(sequence2) // 2]
        print(str(value) + " is in the range 2.")
        checkLessOrGreater(value)
    elif value in sequence3:
        range_median = sequence3[len(sequence3) // 2]
        print(str(value) + " is in the range 3.")
        checkLessOrGreater(value)
    else:
        print("out of the range")


checkValue(131)
