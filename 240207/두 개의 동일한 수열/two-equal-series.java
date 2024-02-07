import java.util.Scanner;
import java.util.Arrays;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System. in);

        int n = sc.nextInt();

        int[] A = new int[n];
        int[] B = new int[n];

        for(int i = 0; i < n; i++){
            A[i] = sc.nextInt();
        }
        for(int i = 0; i < n; i++){
            B[i] = sc.nextInt();
        }

        Arrays.sort(A);
        Arrays.sort(B);
        boolean c = true;

        for(int i = 0; i < n; i++){
            if(A[i] == B[i]){

            }
            else{
                c = false;

                break;

            }

        }

        if(c){
            System.out.printf("Yes");

        }
        else{
            System.out.printf("No");

        }

        



        // 여기에 코드를 작성해주세요.
    }
}