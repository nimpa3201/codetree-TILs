import java.util.Scanner;

public class Main {
    
    public static void main(String[] args) {

        Scanner sc = new Scanner(System. in);

        int n = sc.nextInt();

        System.out.printf("%d",arr(n));
    }

    public static int arr(int n){
        if(n == 1){
            return 1;

        }
        if(n == 2){
            return 2;

        }

        if(n % 2 == 1){
            return n + arr(n- 2);

        }
        else{
            return n + arr(n - 2);

        }
    }
}