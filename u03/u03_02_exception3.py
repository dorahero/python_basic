
import sys

try:
    sys.exit('123')
except SystemExit as e:
    print('接住例外')
    print(e)

try:
    sys.exit('123')
except Exception as e:
    print('接住例外')
    print(e)
