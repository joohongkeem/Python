
import sys
args = sys.argv[1:]       # argv[0] 은 스크립트명 자체!

for x in args:
       print(x, end = " ")
else:
       print()