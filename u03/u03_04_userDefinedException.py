class CustomExceptionError(Exception):      # 自己定義例外類別 直接繼承父類別
    pass

class CustomExceptionError2(Exception):
    def __init__(self, value):
        self.value = value    # 多設定一個屬性
    def __repr__(self):      # 實例化物件後, 呼叫物件時直接將 return 的內容印出在 console
        return self.value

def divide(x, y):
    print('x:', x, 'y:', y)
    t = [type(1), type(1.1)]

    if y == 0:
        raise ZeroDivisionError('不可以除以0')
    elif type(x) not in t or type(y) not in t:
        raise CustomExceptionError('x y 必須為數字')

    result = x / y
    return result

if __name__ == '__main__':
    try:
        print(divide(2, 'a'))
    except Exception as e:   # 接到自定義的例外
        print(e)










