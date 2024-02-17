import java.util.Scanner;

public class Main {
    public static void main(String[] args) {

        Scanner sc = new Scanner(System. in);

        int n = sc.nextInt();
        int k = sc.nextInt();

        int[] arr = new int[n];

        for(int i = 0; i < k; i++){
            int a = sc.nextInt();
            int b = sc.nextInt();

            for(int j = a-1; j < b; j++){
                arr[j]++;

            }
           // System.out.printf("%d %d %d %d %d %d %d\n", arr[0], arr[1], arr[2], arr[3], arr[4], arr[5], arr[6]);
        }
        
        int max = arr[0];

        for(int i = 0; i < n; i++){
            if(arr[i] >= max){
                max = arr[i];

            }
        }
        
        System.out.println(max);




        // 여기에 코드를 작성해주세요.
    }
}