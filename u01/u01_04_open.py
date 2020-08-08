path = 'test.txt'
f = open(path, 'r', encoding='utf-8')
# tmp_str = f.read()
# print(tmp_str)

# tmp_str = f.readline() # 一次印出一行
# print(tmp_str)

# tmp_str = f.readline()
#
# row = 0
# while tmp_str:    # if nothing => return 0
#     print('第 %s row:' %(row), tmp_str, end='')
#     tmp_str = f.readline()       # 每row讀取包含\n
#     row += 1

tmp_str = f.readlines()
print(tmp_str)
for row in tmp_str:
    print(row[:-1])

f.close()       # open 檔案一定要 close

