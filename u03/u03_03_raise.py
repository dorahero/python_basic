def divide(x, y):
    print('x:', x, 'y:', y)
    t = [type(1), type(1.1)]

    if y == 0:
        raise ZeroDivisionError('不可以除以0')
    elif type(x) not in t or type(y) not in t:
        raise TypeError('x y 必須為數字')

    result = x / y
    return result

try:
    print(divide(2, 'a'))
except Exception as e:
    print(e)





