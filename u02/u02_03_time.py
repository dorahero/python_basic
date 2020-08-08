import time
import locale
locale.setlocale(locale.LC_CTYPE, 'chinese')


unix_sec = time.time()
loc_time = time.localtime()
utc_time = time.gmtime()
readable_time = time.asctime()

print('UNIX Time:', unix_sec)
print('local time:', loc_time)
print('GM time:', utc_time)  # 台灣-8
print('readable time:', readable_time)

# 時間日期格式化 => 轉為字串型態
loc_time_str = time.strftime('年份:%Y, %X/%d', loc_time)
print(loc_time_str)

print('\u5e74')




