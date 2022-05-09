def main():
    plate = input("Plate: ").upper()
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def no_punct(p):
    for _ in p :
        if _ in [".", " ", "!"] :
            return True
        else:
            return False


def is_valid(s):
    if 2 <= len(s) <=6 and s[0:2].isalpha() and no_punct(s) is True :
        return True






main()