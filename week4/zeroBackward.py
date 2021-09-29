'''
[동양미래대학교-고급알고리즘(4주차)]
    정수 배열에서 모든 0 값을 찾아 배열의 뒤쪽에 배치시킨다.
    단, 배열 값의 상대적 순서는 유지해야 한다.
    알고리즘의 시간 복잡도는 O(n), 추가 공간은 O(1)로 작성하시오.
    (예) { 2, 3, 4, 0, 6 }의 배열인 경우, { 2, 3, 4, 6, 0 }을 출력한다.

출처) https://www.geeksforgeeks.org/

'''

def swap(A, i, j):
    temp = A[i]
    A[i] = A[j]
    A[j] = temp
 
def partition(A):
    j = 0
    for i in range(len(A)):
        if A[i]:            
            swap(A, i, j)
            j = j + 1
 
 
if __name__ == '__main__':
    A = [6, 0, 8, 2, 3, 0, 4, 0, 1]
    partition(A)
    print(A)