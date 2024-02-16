import java.util.Scanner;

public class Main {
    public static void main(String[] args) {

        Scanner sc = new Scanner(System. in);
        int n = sc.nextInt();

        int[] arr = new int[20];

        int c = 0;

        while(true){

            if(n < 2){
                arr[c++] = n;

                break;
            }

            arr[c++] = n % 2;
            n /= 2;

        }

        for(int i = c -1 ; i >= 0; i--){
            System.out.printf("%d", arr[i]);
            
        }


        // 여기에 코드를 작성해주세요.
    }
}