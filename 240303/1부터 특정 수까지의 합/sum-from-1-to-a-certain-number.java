import java.util.Scanner;


public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System. in);

        int n = sc.nextInt();

        System.out.printf("%d", arr(n));





    }

    public static int arr(int n){
        int c = 0;
        for(int i = 1; i <= n; i++){
            c += i;

        }
        return c / 10;

    }
}