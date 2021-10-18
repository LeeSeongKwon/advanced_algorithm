'''
미로탈출 - BFS
동빈이는N×M크기의직사각형형태의미로에갇혔습니다.미로에는여러마리의괴물이있 어 이를 피해 탈출해야 합니다.
동빈이의위치는(1,1)이며미로의출구는(N,M)의위치에존재하며한번에한칸씩이동할 수 있습니다. 이때 괴물이 있는 부분은 0으로, 괴물이 없는 부분은 1로 표시되어 있습니다. 미로 는 반드시 탈출할 수 있는 형태로 제시됩니다.
이때동빈이가탈출하기위해움직여야하는최소칸의개수를구하세요.칸을셀때는시작칸 과 마지막 칸을 모두 포함해서 계산합니다.

출처) https://www.acmicpc.net/problem/2178
'''
from collections import deque

# BFS 소스코드 구현 
def bfs(x, y):
    # 큐(Queue) 구현을 위해 deque 라이브러리 사용 
    queue = deque()
    queue.append((x, y))
    # 큐가 빌 때까지 반복하기
    while queue:
        x, y = queue.popleft()
        # 현재 위치에서 4가지 방향으로의 위치 확인 
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 미로 찾기 공간을 벗어난 경우 무시
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            #벽인 경우 무시
            if graph[nx][ny] == 0:
                continue
            #해당 노드를 처음 방문하는 경우에만 최단 거리 기록 
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))
    # 가장 오른쪽 아래까지의 최단 거리 반환 
    return graph[n - 1][m - 1]



#N,M을 공백을 기준으로 구분하여 입력 받기 
n, m = map(int, input().split())
# 2차원 리스트의 맵 정보 입력 받기
graph = []
for i in range(n):
    graph.append(list(map(int,
input())))
#이동할 네 가지 방향 정의(상,하,좌,우) dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
# BFS를 수행한 결과 출력 
print(bfs(0, 0))