# 14649. 신용카드 만들기 1

import sys
sys.stdin = open("_신용카드만들기1.txt")

T = int(input())
case_num = 0

for i in range(T):
    case_num += 1
    card_15 = list(map(int, input().split()))

    result = 0

    for i in range(0, 15, 2):
        result += (card_15[i] * 2) #조건1

    for i in range(1, 15, 2):
        result += card_15[i] #조건2

    while (result > 10):
        result -= 10

    print(f"#{case_num} {10 - result}")