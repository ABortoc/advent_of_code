# Part 1
def sum_2020_brute(file, sum):
    with open(file, "r") as reader:
        num_inputs = reader.readlines()
        for num_1 in num_inputs:
            for num_2 in num_inputs:
                if (int(num_1) + int(num_2)) == sum:
                    return print(
                        f"First number is {num_1} and second number is {num_2} and the answer is {int(num_1) * int(num_2)}"
                    )
        return print("Pair doesn't exist")


# sum_2020_brute("input.txt", 2020)


def sum_2020_sorting(file, sum):
    with open(file, "r") as reader:
        num_inputs = [int(x) for x in reader.read().split()]
        sorted_inputs = sorted(num_inputs)
        low = 0
        high = len(sorted_inputs) - 1
        while low < high:
            if (sorted_inputs[low] + sorted_inputs[high]) == sum:
                return print(
                    f"First number is {sorted_inputs[low]} and second number is {sorted_inputs[high]} and the answer is {sorted_inputs[low] * sorted_inputs[high]}"
                )
            elif (sorted_inputs[low] + sorted_inputs[high]) > sum:
                high -= 1
            elif (sorted_inputs[low] + sorted_inputs[high]) < sum:
                low += 1
            else:
                return print("Pair doesn't exist")


# sum_2020_sorting("input.txt", 2020)

# Part 2
def sum_2020_triple_brute(file, sum):
    with open(file, "r") as reader:
        num_inputs = [int(x) for x in reader.read().split()]
        for num_1 in num_inputs:
            for num_2 in num_inputs:
                for num_3 in num_inputs:
                    if (num_1 + num_2 + num_3) == sum:
                        return print(
                            f"{num_1} {num_2} {num_3} product is {num_1 * num_2 * num_3}"
                        )


# sum_2020_triple_brute("input.txt", 2020)


def sum_2020_triple(file, sum):
    with open(file, "r") as reader:
        num_inputs = [int(x) for x in reader.read().split()]
        sorted_inputs = sorted(num_inputs)
        low = 0
        mid = low + 1
        high = len(sorted_inputs) - 1
        while mid < high:
            if (sum - sorted_inputs[low] - sorted_inputs[mid]) in sorted_inputs:
                return print(
                    f"{sorted_inputs[low]} {sorted_inputs[mid]} {sum - sorted_inputs[low] - sorted_inputs[mid]} product is {sorted_inputs[low] * sorted_inputs[mid] * (sum - sorted_inputs[low] - sorted_inputs[mid])}"
                )
            elif (sum - sorted_inputs[low] - sorted_inputs[mid]) > 0:
                mid += 1
            else:
                low += 1
                mid = low + 1


# sum_2020_triple("input.txt", 2020)

