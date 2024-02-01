import java.util.Scanner;

public class Main {
    public static void arr(int x, int y, int[] a){
        int s = 0;

        for(int i = x-1; i < y; i++){
            s += a[i];

        }

        System.out.printf("%d\n", s);
    }
    public static void main(String[] args) {

        Scanner sc = new Scanner(System. in);

        int n = sc.nextInt();
        int m = sc.nextInt();
        int[] A = new int[n];

        for(int i = 0; i < n; i++){
            A[i] = sc.nextInt();

        }

        for(int i = 0; i < m; i++){
            int x = sc.nextInt();
            int y = sc.nextInt();

            arr(x, y, A);
        }


        // 여기에 코드를 작성해주세요.
    }
}