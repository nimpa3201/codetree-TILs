import java.util.Scanner;

public class Main {
    public static int arr(int a){

        if(a < 10){
            return a*a ;

        }
        return arr(a / 10) + (a % 10) * (a % 10);
    }
    public static void main(String[] args) {
        Scanner sc = new Scanner(System. in);

        int n = sc.nextInt();

        System.out.printf("%d", arr(n));



        // 여기에 코드를 작성해주세요.
    }
}