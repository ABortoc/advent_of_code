# Part 1
def check_for_trees(file):
    with open(file, "r") as reader:
        next(reader)
        position = 3
        trees = 0
        for line in reader:
            # While this technically works to just arbitrarilly multiply
            # the string by a big number, there is probably a formulaic way
            # to do this
            tree_line = line[:-1] * 50
            if tree_line[position] == "#":
                trees += 1
            position += 3
        return print(trees)


# check_for_trees("input.txt")

# Part 2
def check_slopes(file, pos):
    with open(file, "r") as reader:
        next(reader)
        position = pos
        trees = 0
        for line in reader:
            tree_line = line[:-1] * 90
            if tree_line[position] == "#":
                trees += 1
            position += pos
        return print(trees)


# check_slopes("input_2.txt", 1)


def check_slopes_two(file, pos):
    with open(file, "r") as reader:
        next(reader)
        next(reader)
        position = pos
        trees = 0
        for line in reader:
            try:
                next(reader)
            except StopIteration:
                continue
            tree_line = line[:-1] * 90
            if tree_line[position] == "#":
                trees += 1
            position += pos
        return print(trees)


# check_slopes_two("input.txt", 1)
