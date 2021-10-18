'''
미로탈출 - BFS
동빈이는N×M크기의직사각형형태의미로에갇혔습니다.미로에는여러마리의괴물이있 어 이를 피해 탈출해야 합니다.
동빈이의위치는(1,1)이며미로의출구는(N,M)의위치에존재하며한번에한칸씩이동할 수 있습니다. 이때 괴물이 있는 부분은 0으로, 괴물이 없는 부분은 1로 표시되어 있습니다. 미로 는 반드시 탈출할 수 있는 형태로 제시됩니다.
이때동빈이가탈출하기위해움직여야하는최소칸의개수를구하세요.칸을셀때는시작칸 과 마지막 칸을 모두 포함해서 계산합니다.

출처) https://www.acmicpc.net/problem/2178
'''

#include <bits/stdc++.h> 
using namespace std;
int n,m;
int graph[201][201];

// 이동할 네 가지 방향 정의 (상, 하, 좌, 우)
int dx[] = {-1, 1, 0, 0}; 
int dy[] = {0, 0, -1, 1};

main(void) {
    cin >> n >> m; 
    for(inti=0;i<n;i++){
        for (int j = 0; j < m; j++) { 
            scanf("%1d", &graph[i][j]);
        } 
    }
    cout << bfs(0, 0) << '\n';
    return 0; 
}


int bfs(int x, int y) {
    // 큐(Queue) 구현을 위해 queue 라이브러리 사용 queue<pair<int, int> > q;
    q.push({x, y});
    // 큐가 빌 때까지 반복하기
    while(!q.empty()) {
        int x = q.front().first;
        int y = q.front().second;
        q.pop();
        // 현재 위치에서 4가지 방향으로의 위치 확인 
        for (int i = 0; i < 4; i++) {
            int nx = x + dx[i];
            int ny = y + dy[i];
            // 미로 찾기 공간을 벗어난 경우 무시
            if (nx < 0 || nx >= n || ny < 0 || ny >= m)
            // 벽인 경우 무시
            if (graph[nx][ny] == 0) continue;
            // 해당 노드를 처음 방문하는 경우에만 최단 거리 기록
            if (graph[nx][ny] == 1) { 
                graph[nx][ny] = graph[x][y] + 1; 
                q.push({nx, ny});
            } 
        }
    }
    // 가장 오른쪽 아래까지의 최단 거리 반환
    return graph[n - 1][m - 1]; 
}