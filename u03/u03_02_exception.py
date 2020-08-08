def createFile(name):
    try:
        with open(name, 'w', encoding='utf-8') as f:   # 別名
            f.write('123')
    except FileNotFoundError as e:           # 接 FileNotFoundError 類別的錯誤訊息
        print(e)
        print(e.args)
        name = name.replace('/', '')
        with open(name, 'w', encoding='utf-8') as f:
            f.write('123')
    except OSError:
        print('OSError: rename %s as test_01.' %(name))
        name = 'test_01'
        with open(name, 'w', encoding='utf-8') as f:
            f.write('123')
    except Exception as e:   # 都沒接到
        print(e)
        print('Unknown Exception!')

createFile('test/test1')    # FileNotFoundError: [Errno 2] No such file or directory: 'test/test1'
createFile('test?test')       # OSError: [Errno 22] Invalid argument: 'test?test'  ? 在 windows 是非法字元











