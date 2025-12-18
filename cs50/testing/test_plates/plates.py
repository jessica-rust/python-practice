import string
def main():
    plate = input("Plate: ").upper()
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if starting_letters(s) and length(s) and numbers(s) and extras(s):
        return True
    else:
        #print("Not all valid")
        return False



def starting_letters(s):
    if s[0:2].isalpha():
        return True
    else:
        #print("start Not valid")
        return False


def length(s):
    if len(s) > 6 or len(s) <= 2:
        #print("length not valid")
        return False

    else:
        return True

def numbers(s):
    nums = []
    for char in s:
        if char.isdigit():
            nums.append(char)

    first_num = None
    i = 0
    while i < len(s):
        if s[i].isdigit():
            first_num = i
            break
        i += 1

    if first_num != None:
        i = first_num
        while i < len(s):
            if not s[i].isdigit():
                return False
            i += 1

    if s[-1:].isalpha():
        if s.isalpha() is False:
            #print("nums ending not valid")
            return False
    if nums:
        if nums[0] == "0":
            #print("nums start with 0")
            return False

    return True


def extras(s):
    for char in s:
        if char.isspace() or char in string.punctuation:
            #print("extras not valid")
            return False
    return True

if __name__ == "__main__":
    main()

