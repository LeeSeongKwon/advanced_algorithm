package week7;

import java.io.*;
import java.util.*;

/**
 * 미로탈출 - DFS
 * 동빈이는N×M크기의직사각형형태의미로에갇혔습니다.미로에는여러마리의괴물이있 어 이를 피해 탈출해야 합니다.
 * 동빈이의위치는(1,1)이며미로의출구는(N,M)의위치에존재하며한번에한칸씩이동할 수 있습니다. 이때 괴물이 있는 부분은 0으로, 괴물이 없는 부분은 1로 표시되어 있습니다. 미로 는 반드시 탈출할 수 있는 형태로 제시됩니다.
 * 이때동빈이가탈출하기위해움직여야하는최소칸의개수를구하세요.칸을셀때는시작칸 과 마지막 칸을 모두 포함해서 계산합니다.
 * 
 * 출처) https://www.acmicpc.net/problem/2178
 * 
 */

public class Maze_DFS {
    public static int N, M;
    public static int[][] graph = new int[200][200]; // 이동할 네 가지 방향 정의{상,하,좌,우}
    public static int dx[] = { -1, 1, 0, 0 };
    public static int dy[] = { 0, 0, -1, 1 };

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in); // N,M 입력
        N = scanner.nextInt();
        M = scanner.nextInt();
        scanner.nextLine(); // 버퍼 지우기 System.out.println("n " + N + "m" + M);
        // 2차원 배열의 정보 입력 받기
        for (int i = 0; i < N; i++) {
            String str = scanner.nextLine();
            for (int j = 0; j < M; j++) {
                graph[i][j] = str.charAt(j) - '0';
                scanner.close();
                System.out.println("result = " + dfs(0, 0));
            }
        }
    }

    private static int dfs(int x, int y) {
        Stack<Node> stack = new Stack<Node>();
        Node node = new Node(x, y);
        stack.push(node);
        while (!stack.empty()) {
            node = stack.pop();
            x = node.getX();
            y = node.getY();
            for (int i = 0; i < 4; i++) {
                int nx = x + dx[i];
                int ny = y + dy[i];
                // 미로 범위를 벗어나면 무시
                if (nx < 0 || ny < 0 || nx >= N || ny >= M)
                    continue;
                // 한 번 왔던 위치면 무시,괴물이 있는 위치면 무시 
                if (graph[nx][ny]==1 ){
                    System.out.println("[" + nx + "," + ny + "]");
                    graph[nx][ny] = graph[x][y] + 1;
                    stack.push(new Node(nx, ny));
                }
            }
        }   
        return graph[N-1][M-1];
    }
 
    static class Node {
        final private int x;
        final private int y;

        Node(int x, int y) {
            this.x = x;
            this.y = y;
        }

        public int getX() {
            return x;
        }

        public int getY() {
            return y;
        }

    }

}



