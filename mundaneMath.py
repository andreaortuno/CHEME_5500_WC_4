def add_even():
    addition = 0
    for i in range(1, 101):
        if i % 2 == 0:
            addition += i

    return addition

print add_even()
