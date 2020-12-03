# Part 1
import re


def check_password(file):
    with open(file, "r") as reader:
        passwords = reader.readlines()
        range_pattern = "\\d+"
        char_pattern = "[a-z]"
        pass_pattern = "\\:\\s(.*)"
        counter_invalid = 0
        counter_total = 0
        for elem in passwords:
            counter_total += 1
            nums = re.findall(range_pattern, elem)
            letter = re.findall(char_pattern, elem)[0]
            pwd = re.search(pass_pattern, elem).group(1)
            upper_char_limit = int(nums[1]) + 1
            match_pattern = f"^(?!(?:.*?{letter}){{{upper_char_limit},}})(?=(?:.*?{letter}){{{nums[0]},}})[a-z]+$"
            correct_password = re.search(match_pattern, pwd)
            if correct_password == None:
                counter_invalid += 1
        return print(counter_total - counter_invalid)


# check_password("input.txt")

# Part 2
def check_password_two(file):
    with open(file, "r") as reader:
        passwords = reader.readlines()
        range_pattern = "\\d+"
        char_pattern = "[a-z]"
        pass_pattern = "\\:\\s(.*)"
        counter_valid = 0
        for elem in passwords:
            nums = re.findall(range_pattern, elem)
            letter = re.findall(char_pattern, elem)[0]
            pwd = re.search(pass_pattern, elem).group(1)
            position_one = int(nums[0]) - 1
            position_two = int(nums[1]) - 1
            if (pwd[position_one] == letter) is not (pwd[position_two] == letter):
                counter_valid += 1
        return print(counter_valid)


# check_password_two("input.txt")
