package week4;
import java.util.Arrays;

/**
 * 정수 배열에서 모든 0 값을 찾아 배열의 뒤쪽에 배치시킨다.
 * 단, 배열 값의 상대적 순서는 유지해야 한다.
 * 알고리즘의 시간 복잡도는 O(n), 추가 공간은 O(1)로 작성하시오.
 * (예) { 2, 3, 4, 0, 6 }의 배열인 경우, { 2, 3, 4, 6, 0 }을 출력한다.
 * 
 * 출처) https://www.geeksforgeeks.org/
 */
class ZeroBackward {
    public static void main(String[] args) {
        int[] A = { 2, 3, 4, 0, 6 };
 
        partition(A);
        System.out.println(Arrays.toString(A));
    }

    public static void swap(int[] A, int i, int j){
        int temp = A[i];
        A[i] = A[j];
        A[j] = temp;
    }
 
    public static void partition(int[] A){
        int j = 0;
 
        for (int i = 0; i < A.length; i++){
            if (A[i] != 0){
                swap(A, i, j);
                j++;
            }
        }
    }
}