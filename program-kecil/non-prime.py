for i in range(100, 0, -1):
    if i == 1:
        print(i, end=" ")
    elif i % 2 == 0 or i % 3 == 0:
        if i in (2, 3):
            continue
        elif i % 3 == 0 and i % 5 == 0:
            print('FooBar', end=" ")
        elif i % 3 == 0:
            print('Foo', end=" ")
        elif i % 5 == 0:
            print('Bar', end=" ")
        else:
            print(i, end=" ")
