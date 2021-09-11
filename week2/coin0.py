'''
[동양미래대학교-고급알고리즘(2주차)]
    * 문제 - 동전0
    준규가 가지고 있는 동전은 총 N종류이고, 각각의 동전을 매우 많이 가지고 있다.
    동전을 적절히 사용해서 그 가치의 합을 K로 만들려고 한다. 이때 필요한 동전 개수의 최솟값을 구하는 프로
    그램을 작성하시오.

출처:https://www.acmicpc.net/problem/11047
'''
N, K = map(int, input().split())
value_list = []
for _ in range(N):
    value = int(input())
    if value <= K:
        value_list.append(value)

cnt = 0
for i in range(len(value_list)):
    value = value_list[(len(value_list))-i-1]
    cnt += (K // value)
    K = K%value

print(cnt)
