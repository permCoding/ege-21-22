
def all_(lst):
    for item in lst:
        if not item:
            return False
    else:
        return True


def any_(lst):
    return True


lst = [True, False, True]

print(all(lst), any(lst))
print(all_(lst), any_(lst))
