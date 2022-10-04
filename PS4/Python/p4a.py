def greater_than_5(x):
    return x > 5

def exists_greater_than_5(x):
    for i in x:
        if greater_than_5(i):
            return True
    return False

def for_all_greater_than_5(x):
    for i in x:
        if not greater_than_5(i):
            return False
    return True
