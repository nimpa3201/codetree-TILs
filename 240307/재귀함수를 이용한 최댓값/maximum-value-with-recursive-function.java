import java.util.Scanner;

public class Main {
    public static int arr2(int n, int[] a){
        int c = 0;
        int s = 0;



        
        if(n == 0){
            c = a[n];

            return c;

        }
        
        return arr2(n - 1, a);

  
    }
    public static void main(String[] args) {

        Scanner sc = new Scanner(System. in);

        int n = sc.nextInt();

        int[] arr = new int[n];

        for(int i = 0; i < n; i++){
            arr[i] = sc.nextInt();

        }
        System.out.printf("%d", arr2(n, arr));

        // 여기에 코드를 작성해주세요.
    }
}