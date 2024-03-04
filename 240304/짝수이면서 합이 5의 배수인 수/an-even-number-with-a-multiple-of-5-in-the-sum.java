import java.util.Scanner;

public class Main{
    public static void main(String[] args) {

        Scanner sc = new Scanner(System. in);

        int n = sc.nextInt();


        System.out.printf("%s", arr(n));


    }

    public static String arr(int n) {
        if(n % 2 == 0 && (n / 10 + (n % 10)) % 5 == 0){
            return "Yes";
        }
        else {
            return "NO";
        }
    }
}