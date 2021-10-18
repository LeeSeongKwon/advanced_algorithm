'''
미로탈출 - DFS
동빈이는N×M크기의직사각형형태의미로에갇혔습니다.미로에는여러마리의괴물이있 어 이를 피해 탈출해야 합니다.
동빈이의위치는(1,1)이며미로의출구는(N,M)의위치에존재하며한번에한칸씩이동할 수 있습니다. 이때 괴물이 있는 부분은 0으로, 괴물이 없는 부분은 1로 표시되어 있습니다. 미로 는 반드시 탈출할 수 있는 형태로 제시됩니다.
이때동빈이가탈출하기위해움직여야하는최소칸의개수를구하세요.칸을셀때는시작칸 과 마지막 칸을 모두 포함해서 계산합니다.

출처) https://www.acmicpc.net/problem/2178
'''

from collections import deque

n, m = map(int, input().split())  # 행, 열
graph = []

# 데이터 받아오기
for i in range(n):
    graph.append(list(map(int, input())))

# 움직임에 따른 네 방향 정의(좌, 우, 상, 하)
dx = [-1, 1, 0, 0]  # 좌우로 움직임
dy = [0, 0, -1, 1]  # 위아래로 움직임


def bfs(x, y):
    queue = deque()  # 큐 구현을 위해 deque 라이브러리 사용
    queue.append((x, y))

    while queue:
        x, y = queue.popleft()  # 기존값 초기화
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
        #  미로 찾기 공간을 벗어난 경우 무시
        if nx < 0 or ny < 0 or nx >= n or ny >= m:
            continue
        # 움직일 수 없는 공간(벽)일 경우 무시
        if graph[nx][ny] == 0:
            continue
        # 노드를 처음 방문하는 경우
        if graph[nx][ny] == 1:
            graph[nx][
                ny] = graph[x][y] + 1  # 기존 좌표(노드)의 값에 +1 한 값을 움직인 좌표(노드)에 추가
            queue.append((nx, ny))

    return graph[n - 1][m - 1]


print(bfs(0, 0))