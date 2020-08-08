import sys

input_args = sys.argv
# 直接接收外部參數(list), element為string
print(input_args)

# 因為第0個是檔案名稱
input_args = input_args[1:]
output = 0
for i in input_args:
    output += int(i)
print(output)
