import java.util.Scanner;

public class Main{
    public static void main(String[] args){
        Scanner sc = new Scanner(System. in);

        int n = sc.nextInt();

        System.out.printf("%d", arr(n));

    }
    public static int arr(int n){
        if(n == 1){
            return 1;

        }

        return arr(n - 1) + n;

    }
}