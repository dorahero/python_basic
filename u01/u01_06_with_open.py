path = 'test.txt'    # 當前路徑下
with open(path, 'r', encoding='utf-8') as f:
    print(f.read())
    # 自動關閉檔案

with open(path, 'a', encoding='utf-8') as f:
    f.write('12313141\n')
