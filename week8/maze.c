'''
미로는 N*M 이진 값을 갖는 배열로 주어진다. 쥐는 (0,0) 즉 maze[0][0]에서 출발하고, 음식은 maze[fx][fy]에 위치한 음식을 찾아 간다.
미로 배열 값의 0은 벽을, 1은 갈 수 있는 경로를 의미한다. 위는 대각선 경로를 제외한 벽이 아닌 모든 경로로 이동할 수 있다.

A Maze is given as N*M binary matrix of blocks and there is a rat initially at (0, 0) ie. maze[0][0] and the rat wants to eat food which is present at
some given block in the maze (fx, fy). In a maze matrix, 0 means that the block is a dead end and 1 means that the block can be used in the path
from source to destination. The rat can move in any direction (not diagonally) to any block provided the block is not a dead end.

출처) https://www.geeksforgeeks.org/
'''
#include <stdio.h>

#define SIZE 5

int maze[SIZE][SIZE] = {
    {0,1,0,1,1},
    {0,0,0,0,0},
    {1,0,1,0,1},
    {0,0,1,0,0},
    {1,0,0,1,0}
};

int solution[SIZE][SIZE];

void printsolution()
{
    int i,j;
    for(i=0;i<SIZE;i++)
    {
        for(j=0;j<SIZE;j++)
        {
            printf("%d\t",solution[i][j]);
        }
        printf("\n\n");
    }
}

int solvemaze(int r, int c)
{
    if((r==SIZE-1) && (c==SIZE-1))
    {
        solution[r][c] = 1;
        return 1;
    }
    if(r>=0 && c>=0 && r<SIZE && c<SIZE && solution[r][c] == 0 && maze[r][c] == 0)
    {
        solution[r][c] = 1;
        if(solvemaze(r+1, c))
            return 1;
        if(solvemaze(r, c+1))
            return 1;
        if(solvemaze(r-1, c))
            return 1;
        if(solvemaze(r, c-1))
            return 1;
        solution[r][c] = 0;
        return 0;
    }
    return 0;

}

int main()
{
    int i,j;
    for(i=0; i<SIZE; i++)
    {
        for(j=0; j<SIZE; j++)
        {
            solution[i][j] = 0;
        }
    }
    if (solvemaze(0,0))
        printsolution();
    else
        printf("No solution\n");
    return 0;
}