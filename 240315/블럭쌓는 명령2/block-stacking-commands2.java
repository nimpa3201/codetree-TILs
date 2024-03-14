import java.util.Scanner;

public class Main {
    public static void main(String[] args) {

        Scanner sc = new Scanner(System. in);

        int n = sc.nextInt();
        int k = sc.nextInt();
        int[] arr = new int[n];

        for(int i = 0; i < k; i++){
            int A = sc.nextInt();
            int B = sc.nextInt();

            for(int j = A-1; j < B; j++){
                arr[j]++;

            }

        }
        int max = 0;

        for(int i = 0; i < n; i++){
            if(max < arr[i]){
                max = arr[i];

            }    

        }

        System.out.printf("%d", max);


        

        // 여기에 코드를 작성해주세요.
    }
}