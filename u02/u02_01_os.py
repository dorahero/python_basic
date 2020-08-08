import os

print('current work dir:', os.getcwd())
print('List dir', os.listdir('../u01'))

# os.mkdir('./test1')
# os.makedirs('./test2/test3')
# os.remove('../u01/test.txt')
# os.rmdir('test2')    # OSError: [WinError 145] 目錄不是空的。: 'test2'
# os.rmdir('test1')
# os.removedirs('./test2/test3')

# test1不存在 => if not False => if True => 創建資料夾
if not os.path.exists('test1'):     # 防止重複創建資料夾的error
    os.mkdir('test1')




