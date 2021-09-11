package week2;
/**
 * [동양미래대학교-고급알고리즘(2주차)]
 * 문제 - 동전0
 * 준규가 가지고 있는 동전은 총 N종류이고, 각각의 동전을 매우 많이 가지고 있다.
 * 동전을 적절히 사용해서 그 가치의 합을 K로 만들려고 한다. 이때 필요한 동전 개수의 최솟값을 구하는 프로
 * 그램을 작성하시오.
 * 
 * 출처:https://www.acmicpc.net/problem/11047
 */
import java.util.Scanner;

public class Coin0 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt(), K = sc.nextInt();

        int[] A = new int[N];
        for (int i = 0; i < N; i++)
            A[i] = sc.nextInt();

        int cnt = 0;
        for (int i = N - 1; i >= 0 && K > 0; i--) {
            cnt += K / A[i];
            K = K % A[i];
        }
        System.out.println(cnt);
    }
}
