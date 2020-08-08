import time

print('123', '321')     # sep預設空白
print('123', '321', sep='')
print('123123', file=open('test.txt', 'w'))   # 輸出到一個新檔案 (檔案名稱, write)
f = open('test.txt', 'a')
for i in range(5):
    time.sleep(5)
    print('1315123123', file=f, flush=True)    # (a = 插入 不會把原本東西刪除)