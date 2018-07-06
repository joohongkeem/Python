# Run module(Hot key : F5)
print("-------------------------------------------------")
print("# 20180705","Made by joohongkeem#".rjust(38),sep=' ',end='\n')
print("-------------------------------------------------")

# 점프투 파이썬 교재 295~ 보면서 정리하기

print("-------------------------------------------------")

    # 3. re 모듈 - 정규식(Regular Expression)
    #
    # - string보다 더 전문적으로 문자열을 다룰 수 있는 모듈
    # - 문자열 내에서 패턴에 매칭되는 문자열을 추출
    #

import re

list = """
Primary Email : joohongkeem@naver.com
Secondary Email : jorange5@naver.com
"""
result_list = re.findall(r"(\w+[\w\.]*)@(\w+[\w\.]*)\.([A-Za-z]+)",list)
print(result_list)          # [('joohongkeem', 'naver', 'com'), ('jorange5', 'naver', 'com')]
for result in result_list:
    print(result)       # ('joohongkeem', 'naver', 'com')
                        # ('jorange5', 'naver', 'com')