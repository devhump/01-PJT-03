#1228. [S/W 문제해결 기본] 8일차 - 암호문1 #D3

import sys
sys.stdin = open("_암호문1.txt")

T = 10
case_num = 0

for i in range(T):
    case_num += 1

    A = int(input())
    list_A = input().split()
    B = int(input())
    list_B = input().split("I ")

    new_list_B = []

    for i in range(1, len(list_B)):
        new_list_B.append(list_B[i])


    # print(f"#{case_num}case")
    # print(A)
    # print(len(list_A))
    # print(B)
    # print(len(new_list_B))

    print(f"#{case_num}case")
    print(A)
    print((list_A))
    print(B)
    print((new_list_B))

    # for i in A:
        
