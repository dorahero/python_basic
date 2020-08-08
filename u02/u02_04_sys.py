import sys

# a = sys.stdin.readline()     # like input
# print(a)

# sys.stdout.write('12314123')   # like print


# sys.stderr = open('stdErr.txt', 'w')  # 將錯誤訊息導向到一個檔案
# a = [1, 2]
# print(a[2])
# sys.stderr = sys.__stderr__  # 改回預設值

# for i in sys.path:       # 和此專案相關的所有目錄
#     print(i)

print('作業系統相關資訊:', sys.platform)

sys.exit('bye')





