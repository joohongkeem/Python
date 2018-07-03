# Run module(Hot key : F5)
print("#20180702","Made by joohongkeem",sep=' ',end='#\n')
print("--------------------------------------")

# 배열의 크기를 입력받고, 그 배열에 정수를 각각 집어넣어보자

arr = []
N = int(input("배열의 크기 ? "))
i=0
while(i<N):
    print(i+1,"번째 값 입력 : ",sep='',end='')
    temp = int(input())
    arr.append(temp)
    i+=1

print("-------------배열 출력-------------")
i=0
while(i<N):
    print("arr[",i,"]=",sep='',end='')
    print(arr[i])
    i+=1
    

