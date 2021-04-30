# Such function is flexible and can handle infinity sequence count and contains a minimum hard coded values
sequence1 = list(range(0, 51))
sequence2 = list(range(80, 101))
sequence3 = list(range(114, 151))
sequences = [sequence1, sequence2, sequence3]


def checkValue(value):
    is_found = False

    def checkLessOrGreater(number):
        if number < range_median:
            print("it is less than {}.".format(range_median))
        elif number == range_median:
            pass
        else:
            print("it is greater than {}.".format(range_median))

    for i in range(len(sequences)):
        if value in sequences[i]:
            is_found = True
            range_median = sequences[i][len(sequences[i]) // 2]

            print("{} is in the range {}.".format(value, i+1))
            checkLessOrGreater(value)

    if not is_found:
        print("out of the range")


checkValue(170)
