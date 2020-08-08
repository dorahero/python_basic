def add(x, y):
    try:
        output = x + y
    except TypeError as e:
        print(e)
        try:
            output = int(x) + int(y)
        except ValueError as e:
            print(e)
            return None
    else:
        print('Answer is', output)
    finally:
        print('The End.')
    return output
print(add(3, '5'))      # TypeError: unsupported operand type(s) for +: 'int' and 'str'
print(add(3, 'x'))
add(3, 5)



