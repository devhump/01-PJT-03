# SWEA_10804.문자열의 거울상 #D3

import sys
sys.stdin = open("_문자열의거울상.txt")

T = int(input())
case_num = 0

for i in range(T):
    case_num += 1
    str_list = input()
    # print(str_list, len(str_list), type(str_list))

    mirror_result = '' # 비어있는 문자열 생성

    for i in range(len(str_list)): #알파벳만 교체해줌

        if str_list[i] == "b":
            mirror_result += "d"
        elif str_list[i] == "d":
            mirror_result += "b"
        elif str_list[i] == "p":
            mirror_result += "q" 
        elif str_list[i] == "q":    
            mirror_result += "p"

    print(f"#{case_num} {mirror_result[::-1]}") # 저장된 순서 반대로 출력
