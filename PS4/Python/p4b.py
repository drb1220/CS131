def does_not_contain_p(x):
    return not "p" in x

def exists_does_not_contain_p(x):
    for i in x:
        if does_not_contain_p(i):
            return True
    return False

def for_all_does_not_contain_p(x):
    for i in x:
        if not does_not_contain_p(i):
            return False
    return True