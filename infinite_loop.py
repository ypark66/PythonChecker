# Infinite Loop
def infinite_recursion(int):
    if int == -1:
        return 0
        int = int + infinite_recursion(int)  # BUG? which spot should be called bug
        return int


def infinite_while_loop(int):
    while int > 0:  # BUG, infinite loop
        int = int + 1


infinite_recursion(1)
infinite_while_loop(1)

