import java.util.Scanner;

public class Main {

    public static int arr(int n){

        if(n == 1){
            return 2;

        }
        else if(n == 2){
            return 4;

        }
        return arr(n - 1) * arr(n - 2);

    }
    public static void main(String[] args) {


        Scanner sc = new Scanner(System. in);

        int n = sc.nextInt();

        System.out.printf("%d", arr(n)%100);

        // 여기에 코드를 작성해주세요.
    }
}